#!/usr/bin/env python3
"""First Custom Code. Just trying out If, elif, Else."""

issues = input("Describe the type of issue:") #user will need to describe type of issue

if issues  == "vpn":
    print ("restart your computer")
elif issues == "Locked out":
    print ("submit a ticket here: https://fanduel.atlassian.net/servicedesk/customer/portal/8/group/30/create/215")
elif issues == "Other":
    print ("Submit a ticket here: https://fanduel.atlassian.net/servicedesk/customer/portal/8/group/62/create/219")

