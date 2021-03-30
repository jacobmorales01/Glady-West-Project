import gladysCompute as compute
import gladysSatellite as satellite
import gladyUserLogin as UserLogin



def runTests():
	'''''
					test functions
					satellite-online
	'''''
					print("running tests")
					
					average=compute 

	def start():
					'''''
											user logged in
					'''''	
					
					userName = userLogin.login()
					
					runApp(userName)
	
def runApp(userName):
			'''''
							running app
			'''''
			
			#loop until user types q
			userQuit = False
			while (not userQuit):
				
					#menu
					
					print("--Welcome to G.W Map App--")
					print("Type T to run startup sequence or q to quit")
					print()
					
					#get first character of input
					userInput =input("Enter a command:")
					lowerInput = userInput.lower()
					firstChar = lowerInput[0:1]d
					
					#shut down
					if firstChar == 'q':
							userQuit = True
					
				# running test sequence
				elif firstChar == 't'
						runTests()
						
				else:
								print("Error:" "+firstChar+" is not a valid command")
								
print :("n")
print("Shutting Down G.Ws Map App")
print :("n")
