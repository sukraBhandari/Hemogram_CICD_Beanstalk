import os
from app import create_app, db
from app.models import User, Role, Privilege, LabProcedure, Patient, Clinic,\
    Order, Event, Sample, Smear, CellImage, Comment, PathReview, Morphology,\
    BloodMorphology, Provider
application = create_app(os.environ.get('LAB_CONFIG'))


@application.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role, Privilege=Privilege,
                LabProcedure=LabProcedure, Patient=Patient, Clinic=Clinic,
                Order=Order, Event=Event, Sample=Sample, Smear=Smear,
                CellImage=CellImage, Comment=Comment, PathReview=PathReview,
                Morphology=Morphology, BloodMorphology=BloodMorphology,
                Provider=Provider)


@application.context_processor
def util_processor():
    """
    Make get_samples function available to templages using context_processor
    """
    def get_pending_samples():
        return Sample.get_pending_data()

    def get_pending_reviews():
        return PathReview.get_pending_data()
    return dict(sample_pending_data=get_pending_samples, review_pending_data=get_pending_reviews)


@application.cli.command()
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=3).run(tests)


@application.cli.command()
def deploy():
    db.create_all()
    Role.preset_roles()


if __name__ == '__main__':
    application.run(debug=True)
