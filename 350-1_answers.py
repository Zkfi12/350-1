import string

certs = {
    "level1" : {
        "True or False: From a security perspective, the best rooms are directly next to emergency exits.": "False",
     
        "From the following choices, select the factors you should consider to understand the threat in your environment.":"Choose all answers.",
        
        "IEDs may come in many forms and may be camouflaged to blend in to the surrounding environment. True or False?":"True.",
     
        "True or False: Surveillance can be performed through either stationary or mobile means.":"True",
     
        "True or False: Terrorists usually avoid tourist locations since they are not DOD-related.":"False",
     
        "True or False: Room invasions are a significant security issue for hotels located in CONUS.":"True",
     
        "Force Protection Condition DELTA means that your base is at which one of the following":"The most increased level of protection",
    
        "True or False: In the event of a skyjacking, you should immediately attempt to subdue the skyjackers.": "False.",
     
        "Persons who have been given access to an installation can be counted on to be of no threat. True or False?": "False",
     
        "Select the factors that will help you avoid becoming the victim of a terrorist attack.": "All (Predictability, Location, Opportunity and Association)",
     
        "True or False: Security is a team effort.": "True.",
     
        "True or False: The initial moments of a hostage taking incident can be extremely dangerous.": "True.",
         
        "Knowing indicators of an unstable person can allow you to identify a potential insider threat before an incident.": "True.",
     
        "True or False: Active resistance should be the immediate response to an active shooter incident.": "False.",
     
        "Which one of the following is NOT an early indicator of a potential insider threat?": "A reasonable disagreement with a US Government Policy.",
     
        "Electronic audio and video devices are never used by terrorists for surveillance purposes. True or False?": "False.",
     
        "Which of the following is not a useful vehicle feature from a security perspective?": "Air bags.",
     
        "True or False: In an active shooter incident involving firearms you should immediately lie on the ground.": "False.",
     
        "True or False: When possible, it is best to always travel with a cell phone.": "True.",
     
        "True or False: State Department Travel Warnings should be consulted prior to taking trips across the US-Mexican border.": "True.",
     
        "True or False: Everyone on an installation has shared responsibility for security.": "True.",
     
        "Alerts from the National Terrorism Advisory System apply only to the United States and its possessions.": "True.",
     
        "True or False: The ticketing area is more secure than the area beyond the security check point.": "False.",
     
        "Home security can be improved with self-help measures like changing locks, securing windows, and improving outdoor lighting. True or False?": "True",
     
        "If you identify a possible surveillance attempt you should try to handle the situation yourself.": "False.",
    
        "True or False: Internet acquaintances can pose a security threat and should be carefully monitored.": "True.",
     
        "Early symptoms of a biological attack may appear the same as common illnesses. True or False?": "True.",
     
        "True or False: Reasons for acquiring hostages include publicity, use as a bargaining chip while executing other crimes, the forcing of political concessions, and ransom.": "True.",
     
        "Which of the following have NOT been targeted or plotted against by terrorists or violent individuals? (Antiterrorism Scenario Training, Page 1)": "none of these answers.",
     
        "Which one of these is a possible indicator of a suspicious letter or package? (Antiterrorism Scenario Training, Page 4)": "Misspellings of common words",
     
        "Which of the following is NOT a recommended response to an active shooter incident? (Antiterrorism Scenario Training, Pages 3 and 4": "Provide instructions to arriving emergency response personnel",
     
        "Keeping a well-maintained vehicle is considered a ""best practice"" from both a security and safety perspective. True or False? (Antiterrorism Scenario Training, Page 2)": "True.",
     
        "Select all factors that are ways in which you might become the victim of a terrorist attack. (Introduction to Antiterrorism, Page 4)": "All",
     
        "What should you NOT do during a hostage rescue attempt? (Antiterrorism Scenario Training, Page 4)": "Try to assist hostage rescue team",
     
        "From an antiterrorism perspective, espionage and security negligence are considered insider threats. (Antiterrorism Scenario Training, Page 2)": "True.",
     
        "Which one of these does NOT pose a risk to security at a government facility? (Antiterrorism Scenario Training, Page 2)": "A person expressing boredom with the US mission",
     
        "Which of the following is NOT an Antiterrorism Level I theme? (Antiterrorism Scenario Training, Page 2)": "Counter-surveillance",       
    },
    
    "cyberawareness": {
        "What conditions are necessary to be granted access to Sensitive Compartmented Information (SCI)?": "Top Secret clearance and indoctrination into the SCI program",
        
        "Which of the following is permitted when using an unclassified laptop within a collateral classified space?": "A Government-issued wired headset with microphone",
        
        "Which of the following is an authoritative source for derivative classification?": "Security Classification Guide",
        
        "Carl receives an e-mail about a potential health risk caused by a common ingredient in processed food. Which of the following actions should Carl NOT take with the e-mail?": "Forward it",
        
        "How can an adversary use information available in public records to target you?": "Combine it with information from other data sources to learn how best to bait you with a scam",
        
        "Which of the following is an appropriate use of government e-mail?": "Using a digital signature when sending attachments",
        
        "Which of the following is NOT a best practice for protecting data on a mobile device?": "Disable automatic screen locking after a period of inactivity",
        
        "Annabeth becomes aware that a conversation with a co-worker that involved Sensitive Compartmented Information (SCI) may have been overheard by someone who does not have the required clearance. What action should Annabeth take?": "Contact her security POC to report the incident.",
        
        "On your home computer, how can you best establish passwords when creating separate user accounts?": "Have each user create their own, strong password",
        
        "Which of the following is an allowed use of government furnished equipment (GFE)?": "Checking personal e-mail if your organization allows it",
        
        "How can you prevent viruses and malicious code?": "Scan all external files before uploading to your computer",
        
        "Which best describes an insider threat? Someone who uses __________ access, ___________, to harm national security through unauthorized disclosure, data modification, espionage, terrorism, or kinetic actions.": "authorized, wittingly or unwittingly",
        
        "Which of the following is an example of behavior that you should report?": "Taking sensitive information home for telework without authorization",
        
        "Which of the following is true of telework?": "You must have permission from your organization to telework.",
        
        "After a classified document is leaked online, it makes national headlines. Which of the following statements is true of the leaked information that is now accessible by the public?": "You should still treat it as classified even though it has been compromised.",
        
        "How should government owned removable media be stored?": "In a GSA-approved container according to the appropriate security classification",
        
        "When linked to a specific individual, which of the following is NOT an example of Personally Identifiable Information (PII)?": "Automobile make and model",
        
        "What does the Common Access Card (CAC) contain?": "Certificates for identification, encryption, and digital signature",
        
        "Sylvia commutes to work via public transportation. She often uses the time to get a head start on work by making phone calls or responding to e-mails on her government approved mobile device. Does this pose a security concern?": "Yes. Eavesdroppers may be listening to Sylvia's phone calls, and shoulder surfers may be looking at her screen. Sylvia should be aware of these risks.",
        
        "Beth taps her phone at a payment terminal to pay for a purchase. Does this pose a security risk?": "Yes, there is a risk that the signal could be intercepted and altered.",
        
        "Which of the following is NOT an appropriate use of your Common Access Card (CAC)?": "Using it as photo identification with a commercial entity",
        
        "When is the safest time to post on social media about your vacation plans?": "After the trip",
        
        "You receive a text message from a package shipper notifying you that your package delivery is delayed due to needing updated delivery instructions from you. It provides a shortened link for you to provide the needed information. You are not expecting a package. What is the best course of action?": "Delete the message",
        
        "Which of the following is NOT a best practice for protecting your home wireless network for telework?": "Use your router's pre-set Service Set Identifier (SSID) and password",
        
        "Which of the following is a best practice for using government e-mail?": "Do not send mass e-mails",
        
        "Your meeting notes are unclassified. This means that your notes": "Do not have the potential to damage national security.",
        
        "What type of information does this personnel roster represent": "Controlled unclassified information (cui)",
        
        "When e-mailing this personnel roster, which of the following should you do?": "All 3- encrypt, digitally, use",
        
        "Select an action to take in response to compromised sensitive compartmented information (sci)": "Call your security point of contact (poc)",
        
        "Select a clue/ laptop- waterjug- printer": "aptop-yes/ waterjug-no/ printer- no",
        
        "which of these individuals demonstrated behavior that could lead to the compromise of SCI": "Col. Cockatiel",
        
        "which of the following poses a physical security risk.": "All 3 choices",
        
        "is this an appropriate use of government-furnished equipment (gfe) sending gov email selling cookies": "no/ all 3 you choices",
        
        "Select the individual who securely authenticates their identity": "Alex. she is her",
        
        "How can malicious code spread": "all except virus scans",
        
        "How can you prevent the download of malicious code": "Scan external files before uploading toy your device Research apps and their vulnerabilities before downloading",
        
        "which of the following may indicate a malicious code attack": "a new app suddenly appears appears on the device, the device slows down, a new tap appears in the web browser",
        
        "It is getting late on Friday. You are reviewing your employees annual self evaluation. Your comments are due on Monday. You can email your employees information to yourself so you can work on it this weekend and go home now. Which method would be the BEST way to send this information?": "Use the government email system so you can encrypt the information and open the email on your government issued laptop",
        
        "What should you do if someone asks to use your government issued mobile device (phone/laptop..etc)?": "Decline to lend your phone / laptop",
        
        "Where should you store PII / PHI?":"Information should be secured in a cabinet or container while not in use",
        
        "Of the following, which is NOT an intelligence community mandate for passwords?": "Maximum password age of 45 days",
        
        "Which of the following is NOT Government computer misuse?": "Checking work email",
        
        "Which is NOT a telework guideline?": "Taking classified documents from your workspace",
        
        "What should you do if someone forgets their access badge (physical access)?": "Alert the security office",
        
        "What can you do to protect yourself against phishing?": "All of the above",
        
        "What should you do to protect classified data?": "Answer 1 and 2 are correct",
        
        "What action is recommended when somebody calls you to inquire about your work environment or specific account information?": "Ask them to verify their name and office number",
        
        "If classified information were released, which classification level would result in ""Exceptionally grave damage to national security""?": "Top Secret",
        
        "Which of the following is NOT considered sensitive information?": "Sanitized information gathered from personnel records",
        
        "Which of the following is NOT a criterion used to grant an individual access to classified data?": "Senior government personnel, military or civilian",
        
        "Of the following, which is NOT a problem or concern of an Internet hoax?": "Directing you to a website that looks real",
        
        "Media containing Privacy Act information, PII, and PHI is not required to be labeled.": "FALSE",
        
        "Which of the following is NOT a home security best practice?": "Setting weekly time for virus scan when you are not on the computer and it is powered off",
        
        "Which of the following best describes wireless technology?": "It is inherently not a secure technology",
        
        "You are leaving the building where you work. What should you do?": "Remove your security badge",
        
        "Which of the following is a good practice to avoid email viruses?": "Delete email from senders you do not know",
        
        "What is considered a mobile computing device and therefore shouldn't be plugged in to your Government computer?":"All of the above",
        
        "Which is NOT a way to protect removable media?": "As a best practice, labeling all classified removable media and considering all unlabeled removable media as unclassified",
        
        "What is NOT Personally Identifiable Information (PII)?": "Hobby",
        
        "Of the following, which is NOT a method to protect sensitive information?": "After work hours, storing sensitive information in unlocked containers, desks, or cabinets if security is not present",
        
        "There are many travel tips for mobile computing. Which of the following is NOT one?": "When using a public device with a card reader, only use your DoD CAC to access unclassified information",
        
        "The use of webmail is": "is only allowed if the organization permits it",
        
        "What is considered ethical use of the Government email system?": "Distributing Company newsletter",
        
        "Which of the following attacks target high ranking officials and executives?": "Whaling",
        
        "What constitutes a strong password?": "all of the above",
        
        "You are logged on to your unclassified computer and just received an encrypted email from a co-worker. The email has an attachment whose name contains the word ""secret"". What should you do?": "Contact your security POC right away",
        
        "Which is a way to protect against phishing attacks?": "Look for digital certificates",
        
        "You receive an email from a company you have an account with. The email states your account has been compromised and you are invited to click on the link in order to reset your password. What action should you take?": "Notify security",
        
        "You are having lunch at a local restaurant outside the installation, and you find a cd labeled ""favorite song"". What should you do?": "Leave the cd where it is",
        
        "How should you securely transport company information on a removable media?": "Encrypt the removable media",
        
        "Should you always label your removable media?": "Yes",
        
        "Which of the following is NOT Protected Health Information (PHI)?": "Medical care facility name",
        
        "If authorized, what can be done on a work computer?": "Check personal email",
        
        "Spear Phishing attacks commonly attempt to impersonate email from trusted entities. What security device is used in email to verify the identity of sender?": "Digital Signatures",
        
        "What type of security is ""part of your responsibility"" and ""placed above all else?""": "Physical",
        
        "If your wireless device is improperly configured someone could gain control of the device? T/F": "true",
        
        "Which of the following is a proper way to secure your CAC/PIV?": "Remove and take it with you whenever you leave your workstation",
        
        "What actions should you take prior to leaving the work environment and going to lunch?": "All of the above",
        
        "P2P (Peer-to-Peer) software can do the following except:": "Allow attackers physical access to network assets",
        
        "What is the goal of an Insider Threat Program?": "Deter, Detect, and Mitigate the risks associated with insider threats",
        
        "Which of the following is not a best practice for traveling overseas with a mobile device?": "store the device in a hotel safe when sightseeing",
        
        "Which of the following uses of removeable media is allowed?": "Government owned removable media that is approved as operationally necessary",
        
        "Which of the following is a best practice when browsing the internet?": "Only accept cookies from reputable, trusted websites",
        
        "Which of the following statements about protected health information PHI is false?": "It is a type of controlled unclassified information",
        
        "You receive an e-mail marked important from your boss asking for data that they need immediately for a meeting starting now. The e-mail was sent from a personal e-mail address that you do not recognize, but it addresses you by name. What concern does this e-mail pose?": "This may be a spear phishing attempt. Contact your boss using contact information that you know to be legitimate.",
        
        "Which of the following is least likely to pose a risk to share on a social networking site?": "Your pet's name",
        
        "how can you protect your home computer?": "turn on the password feature",
        
        "Which of the following is a best practice to protect your identity?": "Order a credit report annually",
        
        "Which of the following is permitted within a Sensitive Compartmented Information Facility (SCIF)?": "An authorized Government-owned Portable Electronic Device (PED)",
        
        "Which of the following uses of removeable media is appropriate?": "Encrypting data stored on removeable media",
        "You receive a phone call offering you a  gift card if you participate in a survey. Which course of action should you take?": "Decline to participate in the survey. This may be a social engineering attempt.",
        
        "Which of the following is true of transmitting or transporting Sensitive Compartmented Information (SCI)?": "Printed SCI must be retrieved promptly from the printer.",
        
        "Under which Cyberspace Protection Condition (CPCON) is the priority focus limited to critical and essential functions?": "CPCON 2",
        
        "Which of the following contributes to your online identity?": "All of these",
        
        "Which of the following is an appropriate use of a DoD Public Key Infrastructure (PKI) token?": "Do not use a token approved for NIPR on SIPR",
        
        "Which of the following statements is true of DoD Unclassified data?": "It may require access and distribution controls",
        
        "Which of the following describes Sensitive Compartmented Information (SCI)? SCI is a program that ____________ various types of classified information into distinct compartments for ________ protection and dissemination or distribution control.": "segregates; added",
        
        "Which type of data could reasonably be expected to cause serious damage to national security?": "secret",
        
        "Which of the following is an example of a strong password?": "d+Uf_4RimUz",
        
        "How can you mitigate the potential risk associated with a compressed URL?": "Use the preview function to see where the link actually leads",
        
        "Which of the following is permitted within a Sensitive Compartmented Information (SCIF)?": "An authorized Government-owned Portable Electronic Device (PED)",
        
        "Which of the following is NOT a best practice for teleworking in an environment where Internet of Things (IoT) devices are present?": "Use the devices' default security settings",
        
        "Which of the following is authoritative source for a derivative classification?": "Security classification guide",
        
        "Terri sees a post on her social media feed that says there is a smoke billowing from the Pentagon. The post includes a video that shows smoke billowing from a building that is not readily identifiable as the Pentagon Jerry is not familiar with the source of the post which of the following describes what Terry has likely seen?": "This is probably a post designed to attract Terri's attention to click on a link and steal her information",
        
        "Which of the following is not appropriate use for your common access card?": "Using it as a photo identification with a commercial entity",
        
        "Which of the following is true of spillage?": "Crap",
        
        "You receive a text message from a package shipper notifying you that your package delivery is delayed due to needing updated delivery instructions from you. It provided a shortened links for you to provide the need information you're not expecting a package what is the best course of action?": "Delete the message",
        
        "Which of the following is true of transmitting or transporting sensitive compartmented information sci?": "Printed SCI must be retrieved properly from the printer",
        
        "Which of the following is the best practice for Physical security?": "Use your own security badge or key code for facility access",
        
        "Which of the following is a step you should not take to protect against spillage?": "Purge any devices memory before connecting it to a classified network",
        
        "Which of the following statements is true of DOD unclassified data?": "It may require access and distribution controls",
        
        
        "Which of the following is not a best practice for protecting your home wireless not work for telework?": "Use your routers preset service, set identifier (SSID) and password",
        
        
        
        
        
        
    },
        
    "infosec": {
        "The Tier 3 Investigation is designated for the following positions:": "Non-critical sensitive.",
        
        "Which of the following methods may be used to transmit Top Secret material?": "- Appropriately cleared courier, - Protected facsimile, message or voice",
        
        "Which of the following is responsible for the review of written materials for public release?": "Defense Office of Republication and Security Review",
        
        "Good Operations Security (OPSEC) practices DO NOT include:": "Discussing sensitive information carefully in public",
        
        "The Physical Security Program is designed to:": "Protect against espionage, sabotage, damage, and theft",
        
        "All of the following are examples of Adverse Information that must be reported EXCEPT:": "Traffic violations with a fine under ",
        
        "You must obtain a defensive foreign travel security briefing prior to travel or at least once a year from whom?": "Security Office",
        
        "What form is used to record the opening and closing of the security container?": "SF702, Security Container Check Sheet",
        
        "In addition to foreign travel requirements, those with SCI access must:": "- Complete a foreign travel questionnaire prior to proceeding on travel, - Complete a secondary questionnaire upon return.",
        
    }    
}

    
def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

def convert_to_lowercase(dictionary):
    if isinstance(dictionary, dict):
        return {remove_punctuation(k.lower()): convert_to_lowercase(v) for k, v in dictionary.items()}
    elif isinstance(dictionary, list):
        return [convert_to_lowercase(item) for item in dictionary]
    else:
        return remove_punctuation(dictionary.lower())
        
certs = convert_to_lowercase(certs)


def main_menu():
    print(certs.keys())
    while True:
        
         print("Welcome to the 350-1 helper.\n")
         print("1. Level 1 Anti-Terrorism")
         print("2. Cyber Awareness")
         print("3. InfoSec")
         user_choice = input("Please enter the number corresponding to the test you would like the answers to:")
         if user_choice == "1":
             anti_terrorism()
             break
         elif user_choice == "2":
             cyber_awareness()
             break
         elif user_choice == "3":
             infosec()
             break
         else:
             print("Please enter a valid choice.")
        

def anti_terrorism():
    while True:
         print("LEVEL 1 ANTI-TERRORISM\n")
         user_input = remove_punctuation(input("Please copy and paste the question here, then press enter to recieve the answer: ")).lower()
         if user_input in certs["level1"]:
             print("Answer: ", certs["level1"][user_input])
             
         else:
             print("Question not found, try another question.")
             
def cyber_awareness():
    while True:
        print("\n")
        print("CYBER AWARENESS\n")
        print("DISCLAIMER!! YOU MUST COPY AND PASTE THE QUESTION.\n")
        user_input = remove_punctuation(input("Please copy and paste the question here, then press enter to recieve the answer: ")).lower()
        if user_input in certs["cyberawareness"]:
            print("Answer: ",certs["cyberawareness"][user_input])  
            
        else:
            print("Question not found, try another question.")
            
def infosec():
    while True:
        print("INFOSEC\n")
        print("DISCLAIMER!! YOU MUST COPY AND PASTE THE QUESTION.\n")
        user_input = remove_punctuation(input("Please copy and paste the question here, then press enter to recieve the answer: ")).lower()
        if user_input in certs["infosec"]:
            print("Answer: ",certs["infosec"][user_input])
            
        else:
            print("Question not found, try another question.")
             
        
    



main_menu()