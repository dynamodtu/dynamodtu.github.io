---
# Template for a new member: copy this file to _members/firstname-lastname.md (without the leading _)
# and fill it in. Files whose name starts with _ are not shown on the site. Leave out any field you don't need.
# M.S., B.S. and special course students don't need a file: add one line to _members/students.md instead.
name: Firstname Lastname
section: phd-students       # pi | postdocs | phd-students | alumni (see member_sections in _config.yml)
order: 1                    # position within the section: 1 = first (top left), then left to right, top to bottom. Give everyone in a section a different number
role: Ph.D. Student
co_supervised:              # true if Tijana is co-supervisor (then `supervisors` are shown on their card)
supervisors:                # optional, with co_supervised: the other supervisors, one per line (main supervisor last),
  - "Anja Boisen"           #   shown as "Co-supervised with ..." on their card
photo: /images/members/firstname-lastname.jpg   # square photo; without one, their initials are shown
research: "Project or research area"   # one short line under their role
email: firstname.lastname@dtu.dk
scholar:
orcid:
linkedin:                   # full profile URL
website:
---

A short description of the person (a sentence or two), shown on their card for postdocs and Ph.D. students.
