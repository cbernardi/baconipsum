import json
import sublime, sublime_plugin
import urllib2

class BaconCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.sel(	)

	def replace(self, sel):
		self.view.insert(edit, "Hello, World!")

# foo = urllib2.urlopen("http://baconipsum.com/api/?paras2&type=meat").read()
