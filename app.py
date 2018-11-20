#!/usr/bin/env python
# -*- coding: utf-8 -*- 
 
from flask import Flask, render_template, request, url_for, redirect
from models import *
from sqlalchemy.sql.expression import func

from os import getenv

app = Flask(__name__)

# Database connection
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


def main():
    # Create tables based on each table definition in `models`
    db.create_all()

    # Initialize with dummy data
    if Feature.query.first() == None:
        f1 = Feature(title="Flannery O'Connor, Mystery and Manners: Occasional Prose", description="Anybody who has survived his childhood has enough information about life to last him the rest of his days.",
                     client="Client A", priority=1, targetDate="01-12-2018", productArea="Policies")
        f2 = Feature(title="Carlos Ruiz Zafón, The Shadow of the Wind", description="A story is a letter that the author writes to himself, to tell himself things that he would be unable to discover otherwise.",
                     client="Client A", priority=2, targetDate="02-12-2018", productArea="Billing")
        f3 = Feature(title="Thomas Mann, Essays of Three Decades", description="A writer is someone for whom writing is more difficult than it is for other people.",
                     client="Client B", priority=1, targetDate="01-12-2018", productArea="Claims")
        f4 = Feature(title="J.D. Salinger, The Catcher in the Rye", description="What really knocks me out is a book that, when you're all done reading it, you wish the author that wrote it was a terrific friend of yours and you could call him up on the phone whenever you felt like it. That doesn't happen much, though.",
                     client="Client c", priority=1, targetDate="03-12-2018", productArea="Reports")

        db.session.add(f1)
        db.session.add(f2)
        db.session.add(f3)
        db.session.add(f4)
        db.session.commit()

        c1 = Client(client="Client A")
        c2 = Client(client="Client B")
        c3 = Client(client="Client C")

        db.session.add(c1)
        db.session.add(c2)
        db.session.add(c3)
        db.session.commit()

        p1 = ProductArea(productArea="Policies")
        p2 = ProductArea(productArea="Billing")
        p3 = ProductArea(productArea="Claims")
        p4 = ProductArea(productArea="Reports")

        db.session.add(p1)
        db.session.add(p2)
        db.session.add(p3)
        db.session.add(p4)
        db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        main()


@app.route("/", methods=['GET', 'POST'])
def index():
    features = Feature.query.all()
    clients = Client.query.all()
    productAreas = ProductArea.query.all()

    # Generating priority list
    max = db.session.query(func.max(Feature.priority)).scalar() + 2
    priorities = range(1, max)

    if request.method == "POST":
        featureTitle = request.form.get("featureTitle")
        featureDescription = request.form.get("featureDescription")
        featureClient = request.form.get("featureClient")
        featureClientPriority = request.form.get("featureClientPriority")
        featureTargetDate = request.form.get("featureTargetDate")
        featureProductArea = request.form.get("featureProductArea")

        feature = Feature(title=featureTitle, description=featureDescription,
                          client=featureClient, priority=featureClientPriority,
                          targetDate=featureTargetDate, productArea=featureProductArea)
        db.session.add(feature)
        db.session.commit()

        features.append({
            "title": featureTitle,
            "description": featureDescription,
            "client": featureClient,
            "priority": featureClientPriority,
            "targetDate": featureTargetDate,
            "productArea": featureProductArea,
        })
        return redirect(url_for('index'))
    return render_template("index.html",
                           clients=clients,
                           priorities=sorted(priorities),
                           productAreas=productAreas,
                           features=features
                           )
