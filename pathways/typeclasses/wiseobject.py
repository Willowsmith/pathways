from random import choice
from typeclasses.objects import Object

class WiseObject(Object):
	"""
	An object speaking when someone looks at it.
	"""
	def at_object_creation(self):
		"Called when object is first created"
		self.db.wise_texts = \
			   ["Tomorrow is another day, just don't depend on there being one.", 
			    "Live life to the fullest, you only have the one.", 
			     "Be kind to one another, hurting another isn't worth the karma."]

	def return_appearance(self, looker):
		"""
		Called by the look command. We want to return 
		wisdom when we get looked at.
		"""
		# first get the base string from the
		#parent's return_appearance.
		string = super(WiseObject, self).return_appearance(looker)
		wisewords = "\n\nIt grumbles and says: '%s'"
		wisewords = wisewords % choice(self.db.wise_texts)
		return string + wisewords