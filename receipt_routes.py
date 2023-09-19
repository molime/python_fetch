from app import app
from flask import request, jsonify
from db_operations import db, Receipts, Items

from functions import alpha_numeric, round_dollar, multiple_quarter, items_even, description_length, date_odd, purchase_time


@app.route("/receipts/process", methods=["POST"])
def process_receipts():
    data = request.get_json()
    receipt = Receipts(retailer=data["retailer"], purchaseDate=data["purchaseDate"],
                       purchaseTime=data["purchaseTime"], total=data["total"])

    db.session.add(receipt)
    db.session.commit()
    for item in data["items"]:
        item = Items(shortDescription=item["shortDescription"],
                     price=item["price"], receipt=receipt.id)
        db.session.add(item)
    db.session.commit()

    return jsonify({"id": receipt.id}), 200


@app.route("/receipts/<_id>/points", methods=["GET"])
def get_points(_id):
    receipt = Receipts.query.filter_by(id=_id).first()
    if receipt is None:
        return jsonify({"error": "Not found!"}), 404
    items = Items.query.filter_by(receipt=receipt.id).all()

    points = alpha_numeric(receipt_name=receipt.retailer)
    points += round_dollar(amount=receipt.total)
    points += multiple_quarter(amount=receipt.total)
    points += items_even(list_length=len(items))
    for item in items:
        points += description_length(description=item.shortDescription,
                                     price=float(item.price))
    points += date_odd(date=receipt.purchaseDate)
    points += purchase_time(time=receipt.purchaseTime)
    return jsonify({"points": points}), 200
