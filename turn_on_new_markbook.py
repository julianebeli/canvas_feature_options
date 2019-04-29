'''
A list of institution wide feature options are available at: https://tas.instructure.com//api/v1/accounts/1/features

The result has a feature attribute.

The new gradebook feature attribute is: "feature": "new_gradebook":

There is a ‘state’ attribute which controls if the feature is [on, off, allowed]

This attribute can be changed in courses.

The call is

PUT /api/v1/courses/:course_id/features/flags/:feature

State = "on"

This call will fail if a parent account sets a feature flag for the same feature in any state other than “allowed”.
'''
import json
import __init__
from api.requestor2 import API

api = API('beta')


def action(course):
    print(f"doing {course['id']}")
    # /v1/courses/{course_id}/features/flags/{feature}
    params = dict(methodname='set_feature_flag_courses',
                  course_id=course['id'],
                  feature='new_gradebook',
                  state='on')
    api.add_method(**params)
    api.do()
    print(api.results)


allowed_term_ids = [1, 35, 38, 41, 42]
with open('course_details.json') as f:
    course_info = json.loads(f.read())


for school in course_info:
    [school_name, courses] = school
    print(school_name['name'])
    for course in courses:
        if course['term_id'] in allowed_term_ids:
            action(course)


# get subaccount ids recursively
# use PUT /api/v1/accounts/:account_id/features/flags/:feature
# https://tas.beta.instructure.com/courses/28979/settings
# /api/v1/accounts/38/features/flags/new_gradebook
