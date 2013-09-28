from polls.models import Poll, Choice # Import the model classes we just wrote.

# No polls are in the system yet.
Poll.objects.all()

# Create a new Poll
# Support for time zones is enabled in the default settings file, so
# Django expects a timedate with tzinfo for pub_date. Use timezone.now()
# instead of datetime.datetime.now() and it will do the right thing.
from django.utils import timezone
p = Poll(question="What's new?", pub_date=timezone.now())

# Save the object into the database. You have to call save() explicitly.
p.save()

# Now it has an ID. Note that this might say "1L" instead of "1", depending 
# on which database you're using. That's no biggie; it just means your
# database backend prefers to return integers as Python long integer
# objects.
p.id

# Access database columns via Python attributes
p.question
p.pub_date

# Change values by changing the attributes, then calling save().
p.question = "What's up?"
p.save()

# objects.all() displays all the polls in the database
Poll.objects.all()

