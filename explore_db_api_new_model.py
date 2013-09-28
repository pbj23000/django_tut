from polls.models import Poll, Choice 

# Make sure our __unicode__() addition worked.
Poll.objects.all()

# Django provides a rich database lookup API that's entirely driven by
# keyword arguments.
Poll.objects.filter(id=1)
Poll.objects.filter(question__startswith='What')

# Get the poll that was published this year.
from django.utils import timezone
current_year = timezone.now().year
Poll.objects.get(pub_date__year=current_year)

# Request an ID that doesn't exist, this will raise an exception.
Poll.objects.get(id=2)

# Lookup by a primary key is the most common case, so Django provides a 
# shortcut for primary key exact lookups.
# The following is identical to Poll.objects.get(id=1)
Poll.objects.get(pk=1)

# Make sure our custom method worked.
p = Poll.objects.get(pk=1)
p.was_published_recently()

# Give the Poll a couple of Choices. The create call constructs a new 
# Choice object, does the INSERT statement, adds the choice to the set
# of available choices and returns the new Choice object. Django creates
# a set to hold the "other side" of a ForeignKey relation
# (e.g. a poll's choices) which can be accessed via the API.
p = Poll.objects.get(pk=1)

# Display any choices from the related object set -- none so far.
p.choice_set.all()

# Create three choices
p.choice_set.create(choice_text='Not much', votes=0)
p.choice_set.create(choice_text='The sky', votes=0)
c = p.choice_set.create(choice_text='Just hacking again', votes=0)

# Choice objects have API access to their related Poll objects.
c.poll

# And vica versa: Poll objects get access to Choice objects.
p.choice_set.all()
p.choice_set.count()

# The API automatically follows relationships as far as you need.
# Use double underscores to separate relationships.
# This works as many levels deep as you want; there's no limit.
# Find all Choices for any poll whose pub_date is in this year
# [reusing the 'current_year' variable we created above).
Choice.objects.filter(poll__pub_date__year=current_year)

# Let's delete one of the choices. Use delete() for that.
c = p.choice_set.filter(choice_text__startswith='Just hacking')
c.delete()

