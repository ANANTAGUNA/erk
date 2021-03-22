from erk import *

class BlankPlugin(Plugin):
	"""
		This is a basic "blank" Ərk plugin with all the
		event methods available. Just change the name of
		the class, change the "name", "version", and
		"description" class attributes, and you're half-
		way to writing an Ərk plugin!
	"""

	name = "Blank Plugin"
	version = "1.0"
	description = "This is a blank plugin"

	def action(self,target,user,message):
		"""
			Triggers when the client receives a CTCP Action message.

			target (string): the channel or nickname it was sent to
			user (string): the user who sent the message
			message (string): the message
		"""
		pass

	def ctcp(self,user,target,tag,message):
		"""
			Triggers when the client receives an otherwise unrecognized
			CTCP message.

			user (string): the user who sent the message
			target (string): the channel or nickname it was sent to
			tag (string): the tag attached to the message
			message (string): the message
		"""
		pass

	def input(self,window,text):
		"""
			Triggers when a user enters text into the text entry
			widget and presses return. Return True to stop processing
			the entry text, and return False or None to allow Ərk
			to continue processing the input.

			window (string): the name of the window the text was
			                 entered into. This will be set to
			                 None if the text was entered into
			                 a server console window
			text (string): the text that was entered
		"""
		pass

	def join(self,channel,user):
		"""
			Triggers when a user joins a channel that Ərk
			is "present" in.

			channel (string): the name of the channel joined
			user (string): the user that joined the channel
		"""
		pass

	def joined(self,channel):
		"""
			Triggers when Ərk joins a channel

			channel (string): the name of the channel joined
		"""
		pass

	def kick(self,channel,kickee,kicker,message):
		"""
			Triggers when a user is kicked from a channel that
			Ərk is "present" in.

			channel (string): the channel the user was kicked out of
			kickee (string): the user that was kicked out
			kicker (string): the user that issued the kick command
			message (string): the kick message
		"""
		pass

	def kicked(self,channel,kicker,message):
		"""
			Triggers when Ərk is kicked out of a channel.

			channel (string): the channel Ərk was kicked out of
			kicker (string): the user that kicked Ərk out
			message (string): the kick message
		"""
		pass

	def line_in(self,line):
		"""
			Triggers when Ərk receives data from a server.

			line (string): the data received
		"""
		pass

	def line_out(self,line):
		"""
			Triggers when Ərk sends data to a server.

			line (string): the data sent
		"""
		pass

	def mode(self,channel,user,mset,modes,args):
		"""
			Triggers when Ərk receives a mode notification.

			channel (string): the target of the mode set (usually a channel)
			user (string): the user that set the mode
			mset (boolean): True if the mode is being set, False if the mode
			                is being "unset" (removed)
			modes (string): the modes be set or unset
			args (list): any arguments to the modes being set
		"""
		pass

	def motd(self,motd_message):
		"""
			Triggers when Ərk receives a server's "Message of
			the Day".

			motd_message (list): the server's MOTD, one line per list entry
		"""
		pass

	def notice(self,target,user,message):
		"""
			Triggers when Ərk receives a notice message.

			target (string): the targer of the message (may be a channel or nickname)
			user (string): the user that sent the message
			message (string): the message
		"""
		pass

	def part(self,channel,user):
		"""
			Triggers when a user leaves a channel that Ərk
			is "present" in.

			channel (string): the name of the channel left
			user (string): the user that left the channel
		"""
		pass

	def parted(self,channel):
		"""
			Triggers when Ərk leaves a channel

			channel (string): the name of the channel left
		"""
		pass

	def private(self,user,message):
		"""
			Triggers when Ərk receives a private message.

			user (string): the user that sent the message
			message (string): the message
		"""
		pass

	def public(self,channel,user,message):
		"""
			Triggers when Ərk receives a public message (channel chat).

			channel (string): the channel the message was sent from
			user (string): the user that sent the message
			message (string): the message
		"""
		pass

	def quit(self,nickname,message):
		"""
			Triggers when a user quits IRC (disconnects from the server).

			nickname (string): the nickname of the user that quit
			message (string): the quit message left by the user
		"""
		pass

	def registered(self):
		"""
			Triggers when Ərk completes connection with
			an IRC server.
		"""
		pass

	def tick(self,uptime):
		"""
			Triggers once a second while Ərk is connected to
			a server.

			uptime (integer): how many seconds Ərk has been connected
			                  to the server that triggered the event.
		"""
		pass
