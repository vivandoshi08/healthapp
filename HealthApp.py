import math
import os
import sys
from colors import *


class Cancer:
	def cancertest():
		acancer = input("Do you have hoarseness?(y,n): ")
		bcancer = input("Do you have an obvious change in wart or a mole?(y,n): ")
		ccancer = input("Do you have unexplained weight loss?(y,n): ")
		dcancer = input("Do you have indigestion or difficulty swallowing?(y,n): ")
		ecancer = input("Do you have blood in urine?(y,n): ")
		fcancer = input("Do you have persistent lumps or swollen glands?(y,n): ")
		cancerprobability = 0
		if acancer == "y":
			cancerprobability += 1
		if bcancer == "y":
			cancerprobability += 1
		if ccancer == "y":
			cancerprobability += 1
		if dcancer == "y":
			cancerprobability += 1
		if ecancer == "y":
			cancerprobability += 1
		if fcancer == "y":
			cancerprobability += 1
		print("Out of the 6 questions,", cancerprobability, " tested positive")
		print("for cancer.")
		if cancerprobability>4:
			print("You have a high chance of cancer. Please visit your doctor immediately.")
		elif cancerprobability<=4 and cancerprobability>0:
			print("Your chances of cancer are minor. You should visit the doctor for ways to")
			print("address minor sicknesses that you may have.")
		else:
			print("You have a very low chance of getting cancer.Woo-Hoo!")
		cancermenu = input("Do you want to go back to the health menu? (y,n) ")
		if cancermenu == "y":
			mainif()
		else:
			print("Thank you for using Vivan Doshi's Health App.")
class Diabetes:
	def diabetessyptoms():
		adiabetes = input("Do you have increased thirst?(y,n): ")
		bdiabetes = input("Do you have increased hunger especially after eating?(y,n): ")
		cdiabetes = input("Do you unexplained weight loss even though you are eating and you feel hungry?(y,n): ")
		ddiabetes = input("Do you have constant headaches?(y,n): ")
		ediabetes = input("Are you usually feeling fatigue?(y,n): ")
		fdiabetes = input("Do you frequently urinate or have urine infections?(y,n): ")
		gdiabetes = input("Do you have a dry mouth many times(y,n): ")
		hdiabetes = input("Do you have blurred vision?(y,n): ")
		diabetesprob = 0
		if adiabetes == "y":
			diabetesprob += 1
		if bdiabetes == "y":
			diabetesprob += 1
		if cdiabetes == "y":
			diabetesprob += 1
		if ddiabetes == "y":
			diabetesprob += 1
		if ediabetes == "y":
			diabetesprob += 1
		if fdiabetes == "y":
			diabetesprob += 1
		if gdiabetes == "y":
			diabetesprob += 1
		if hdiabetes == "y":
			diabetesprob += 1
		print("Out of the 8 questions,you got",diabetesprob, "tested positive for diabetes.")
		if diabetesprob>=5:
			print("You have a high chance of diabetes. Please visit your doctor immediately.")
		elif diabetesprob<=4 and diabetesprob>0:
			print("Your chances of diabetes are minor. You should visit the doctor for ways to")
			print("address minor sicknesses that you may have.")
		else:
			print("You have a very low chance of getting diabetes.Woo-Hoo!")
		diabetesmenu = input("Do you want to go back to the health menu? (y,n) ")
		if diabetesmenu == "y":
			mainif()
		else:
			print("Thank you for using Vivan Doshi's Health App.")
class HeartAttack:
	def Heartattacksymptoms():
		aHA = input("Do you have chest discomfort?(y,n): ")
		bHA = input("Do you have discomfort in other areas of the upper body like pain in the arms,back,neck,jaw,or stomach?(y,n): ")
		cHA = input("Do you have shortness in breath with or without chest discomfort?(y,n): ")
		dHA = input("Do you most of the time break out a cold sweat?(y,n): ")
		eHA = input("Do you have nausea sometimes?(y,n): ")
		fHA = input("Do you feel like having lightheadedness?(y,n): ")
		HAprob = 0
		if aHA == "y":
			HAprob += 1
		if bHA == "y":
			HAprob += 1
		if cHA == "y":
			HAprob += 1
		if dHA == "y":
			HAprob += 1
		if eHA == "y":
			HAprob += 1
		if fHA == "y":
			HAprob += 1
		print("Out of 6 questions, You had",HAprob,"claimed to be positive.")
		if HAprob > 3:
			print("You have a high chance of having a heart attack. Go to your doctor immediately.")
		elif HAprob <= 3 and HAprob > 0:
			print("You have a slight chance of having a heart attack. Go to your doctor to have an appointment on you for a heart attack.")
		elif HAprob == 0:
			print("You don't have any chance of having a heart attack soon. Woo-Hoo!")
		HAmenu = input("Do you want to go back to the health menu?(y,n): ")
		if HAmenu == "y":
			mainif()
		else:
			print("Thank you for using Vivan's health app. I hope you have a n")
class pneumonia:
	def pneumoniatest():
		apn = input("Do you have chest pain when you breathe or cough?(y,n): ")
		bpn = input("Do you have confusion or changes in mental awareness?(y,n): ")
		cpn = input("Do you have cough which may produce phlegm?(y,n): ")
		dpn = input("Do you have fatigue?(y,n): ")
		epn = input("Do you have fever, sweating, and shaking chills?(y,n): ")
		pnprob = 0
		if apn == "y":
			pnprob += 1
		if bpn == "y":
			pnprob += 1
		if cpn == "y":
			pnprob += 1
		if dpn == "y":
			pnprob += 1
		if epn == "y":
			pnprob += 1
		print("Out of 5 questions, You had",pnprob,"claimed to be positive.")
		if pnprob >= 3:
			print("You have a high chance of having pneumonia. Go to your doctor immediately.")
		elif pnprob <= 2 and pnprob > 0:
			print("You have a slight chance of having pneumonia. Go to your doctor to have an appointment on you for pneumonia.")
		elif pnprob == 0:
			print("You don't have any chance of having pneumonia soon. Woo-Hoo!")
		pnmenu = input("Do you want to go back to the health menu?(y,n): ")
		if pnmenu == "y":
			mainif()
		else:
			print("Thank you for using Vivan's health app. I hope you have a nice day.")
class bronchitasChitas:
	def Bc():
		abc = input("Do you cough with clear,yellow or green sputum(the gunk you cough up)?(y,n): ")
		bbc = input("Do you have fatigue?(y,n): ")
		cbc = input("Are you usually wheezing?(y,n): ")
		dbc = input("Do you have a runny, stuffy nose occuring before chest congestion begins?(y,n): ")
		ebc = input("Do you have a shortness of breath,usually following a coughing jag?(y,n): ")
		fbc = input("Do you have discomfort in the center of the chest due to cough?(y,n): ")
		gbc = input("Do you have mild fever?(y,n): ")
		bcprob = 0
		if abc == "y":
			bcprob += 1
		if bbc == "y":
			bcprob += 1
		if cbc == "y":
			bcprob += 1
		if dbc == "y":
			bcprob += 1
		if ebc == "y":
			bcprob += 1
		if fbc == "y":
			bcprob += 1
		if gbc == "y":
			bcprob += 1
		print("Out of 7 questions, You had",bcprob,"claimed to be positive.")
		if bcprob >= 4:
			print("You have a high chance of having bronchitas chitas. Go to your doctor immediately.")
		elif bcprob <= 3 and bcprob > 0:
			print("You have a slight chance of having bronchitas chitas. Go to your doctor to have an appointment on you for bronchitas chitas.")
		elif bcprob == 0:
			print("You don't have any chance of having bronchitas chitas soon. Woo-Hoo!")
		bcmenu = input("Do you want to go back to the health menu?(y,n): ")
		if bcmenu == "y":
			mainif()
		else:
			print("Thank you for using Vivan's health app. I hope you have a nice day.")


class Asthma:
	def asthmatest():	
		aA = input("Do you have shortness of breath?(y,n): ")
		bA = input("Do you have chest tightness or pain?(y,n): ")
		cA = input("Do you have trouble sleeping caused by shortness of breath,coughing or wheezing?(y,n): ")
		dA = input("Do you have a whistling or wheezing sound when exhaling?(y,n): ")
		Aprob = 0
		if aA == "y":
			Aprob+=1
		if bA == "y":
			Aprob+=1
		if cA == "y":
			Aprob+=1
		if dA == "y":
			Aprob+=1
		print("Out of the 4 questions,",Aprob,"were tested positive.")
		if Aprob >= 3:
			print("You have a high chance of having asthma. Go to your doctor immediately.")
		elif Aprob <= 2 and Aprob > 0:
			print("You have a slight chance of having asthma. Go to your doctor to have an appointment on you for asthma.")
		elif Aprob == 0:
			print("You don't have any chance of having asthma soon. Woo-Hoo!")
		Amenu = input("Do you want to go back to the health menu?(y,n): ")
		if Amenu == "y":
			mainif()
		else:
			print("Thank you for using Vivan's health app. I hope you have a nice day.")
class Turbeloscis:
	def Turbotest():
		aTB = input("Do you have coughing that lasts three or more weeks?(y,n): ")
		bTB = input("Do you cough up blood?(y,n): ")
		cTB = input("Do you have chest pain, or pain with breathing or coughing?(y,n): ")
		dTB = input("Do you have unintentional weight loss?(y,n): ")
		eTB = input("Do you have fatigue?(y,n): ")
		fTB = input("Do you have fever?(y,n): ")
		gTB = input("Do you have night sweats?(y,n): ")
		hTB = input("Do you have chills?(y,n): ")
		TBprob = 0
		if aTB == "y":
			TBprob+=1
		if bTB == "y":
			TBprob+=1
		if cTB == "y":
			TBprob+=1
		if dTB == "y":
			TBprob+=1
		if eTB == "y":
			TBprob+=1
		if fTB == "y":
			TBprob+=1
		if gTB == "y":
			TBprob+=1
		if hTB == "y":
			TBprob+=1
		print("Out of the 8 questions,",TBprob,"were tested positive.")
		if TBprob >= 5:
			print("You have a high chance of having turberculosis. Go to your doctor immediately.")
		elif TBprob <= 4 and TBprob > 0:
			print("You have a slight chance of having turberculosis. Go to your doctor to have an appointment on you for turberculosis.")
		elif TBprob == 0:
			print("You don't have any chance of having turberculosis soon. Woo-Hoo!")
		TBmenu = input("Do you want to go back to the health menu?(y,n): ")
		if TBmenu == "y":
			mainif()
		else:
			print("Thank you for using Vivan's health app. I hope you have a nice day.")

class Alzheimerss:
	def alz_test():
		aAlz = input("Do you have memory loss that disrupts daily life?(y,n): ")
		bAlz = input("Do you have challenges in planning or solving problems?(y,n): ")
		cAlz = input("Do you have difficulty completing familiar tasks at home,at work, or at lesiure?(y,n): ")
		dAlz = input("Do you have confusion with time or place?(y,n): ")
		eAlz = input("Do you have trouble understanding visual images and spatual relationships?(y,n): ")
		Alzprob = 0
		if aAlz == "y":
			Alzprob += 1
		if bAlz == "y":
			Alzprob += 1
		if cAlz == "y":
			Alzprob += 1
		if dAlz == "y":
			Alzprob += 1
		if eAlz == "y":
			Alzprob += 1
		print("Out of 5 questions, You had",Alzprob,"claimed to be positive.")
		if Alzprob >= 3:
			print("You have a high chance of having Alzheimer's. Go to your doctor immediately.")
		elif Alzprob <= 2 and Alzprob > 0:
			print("You have a slight chance of having Alzheimer's. Go to your doctor to have an appointment on you for Alzheimers.")
		elif Alzprob == 0:
			print("You don't have any chance of having Alzheimer's soon. Woo-Hoo!")
		Alzmenu = input("Do you want to go back to the health menu?(y,n): ")
		if Alzmenu == "y":
			mainif()
		else:
			print("Thank you for using Vivan's health app. I hope you have a nice day.")

class Cholesterol:
	def cholestroltest():
		aC = input("Do you have angina, chest pain?(y,n): ")
		bC = input("Do you have nausea?(y,n): ")
		cC = input("Do you have extreme fatigue?(y,n): ")
		dC = input("Do you have shortness of breath?(y,n): ")
		eC = input("Do you have pain in the neck, jaw, upper abdomen, or back?(y,n): ")
		fC = input("Do you have numbness or coldness in your extremities?(y,n): ")
		Cprob = 0
		if aC == "y":
			Cprob += 1
		if bC == "y":
			Cprob += 1
		if cC == "y":
			Cprob += 1
		if dC == "y":
			Cprob += 1
		if eC == "y":
			Cprob += 1
		print("Out of 6 questions, You had",Cprob,"claimed to be positive.")
		if Cprob >= 4:
			print("You have a high chance of having cholesterol. Go to your doctor immediately.")
		elif Cprob <= 2 and Cprob > 0:
			print("You have a slight chance of having cholesterol. Go to your doctor to have an appointment on you for cholesterol.")
		elif Cprob == 0:
			print("You don't have any chance of having cholesterol soon. Woo-Hoo!")
		Cmenu = input("Do you want to go back to the health menu?(y,n): ")
		if Cmenu == "y":
			mainif()
		else:
			print("Thank you for using Vivan's health app. I hope you have a nice day.")

class Diarrheaa:
	def diarrheatest():
		ad = input("Do you have loose, watery stools?(y,n): ")
		bd = input("Do you have abdominal cramps?(y,n): ")
		cd = input("Do you have abdominal pain?(y,n): ")
		dd = input("Do you have fever?(y,n): ")
		ed = input("Do you have blood in the stool?(y,n): ")
		gd = input("Do you have bloating?(y,n): ")
		hd = input("Do you have urgent need to have a bowel movement?(y,n): ")
		Dprob = 0
		if ad == "y":
			Dprob+=1
		if bd == "y":
			Dprob+=1
		if cd == "y":
			Dprob+=1
		if dd == "y":
			Dprob+=1
		if ed == "y":
			Dprob+=1
		if gd == "y":
			Dprob+=1
		if hd == "y":
			Dprob+=1
		print("Out of the 7 questions,",Dprob,"were tested positive.")
		if Dprob >= 4:
			print("You have a high chance of having Diarrhea. Go to your doctor immediately.")
		elif Dprob <= 3 and Dprob > 0:
			print("You have a slight chance of having Diarrhea. Go to your doctor to have an appointment on you for Diarrhea.")
		elif Dprob == 0:
			print("You don't have any chance of having Diarrhea soon. Woo-Hoo!")
		dmenu = input("Do you want to go back to the health menu?(y,n): ")
		if dmenu == "y":
			mainif()
		else:
			print("Thank you for using Vivan's health app. I hope you have a nice day.")
class Dehydration:	
	def dehy():
		aD = input("Do you have increased thirst?(y,n): ")
		bD = input("Do you cough a dry mouth?(y,n): ")
		cD = input("Do you unusually become tired or sleepy?(y,n): ")
		dD = input("Do you have decreased urine output?(y,n): ")
		eD = input("Do you have urine that is low volume and more yellowish than normal?(y,n): ")
		fD = input("Do you have an unusual amount of headaches?(y,n): ")
		gD = input("Do you have dry skin?(y,n): ")
		hD = input("Do you have an unusual amount of dizziness?(y,n): ")
		Dprob = 0
		if aD == "y":
			Dprob+=1
		if bD == "y":
			Dprob+=1
		if cD == "y":
			Dprob+=1
		if dD == "y":
			Dprob+=1
		if eD == "y":
			Dprob+=1
		if fD == "y":
			Dprob+=1
		if gD == "y":
			Dprob+=1
		if hD == "y":
			Dprob+=1
		print("Out of the 8 questions,",Dprob,"were tested positive.")
		if Dprob >= 5:
			print("You have a high chance of having dehydration. Go drink some water really soon.")
		elif Dprob <= 4 and Dprob > 0:
			print("You have a slight chance of having dehydration. Go drink some water in five minutes at most.")
		elif Dprob == 0:
			print("You don't have any chance of having dehydration soon. Woo-Hoo!")
		Dmenu = input("Do you want to go back to the health menu?(y,n): ")
		if Dmenu == "y":
			mainif()
		else:
			print("Thank you for using Vivan's health app. I hope you have a nice day.")
class HeatStroke:
	def HS():
		ah = input("Do you have throbbing headaches?(y,n): ")
		bh = input("Do you have lightheadedness?(y,n): ")
		ch = input("Do you have lack of sweating despite the heat?(y,n): ")
		dh = input("Do you have red,hot and dry skin?(y,n): ")
		eh = input("Do you have muscle weakness or cramps?(y,n): ")
		fh = input("Do you have nausea and vomit?(y,n): ")
		gh = input("Do you have rapid heartbeat, which may be either strong or weak?(y,n): ")
		hh = input("Do you have rapid,shallow breathing?(y,n): ")
		hprob = 0
		if ah == "y":
			hprob+=1
		if bh == "y":
			hprob+=1
		if ch == "y":
			hprob+=1
		if dh == "y":
			hprob+=1
		if eh == "y":
			hprob+=1
		if fh == "y":
			hprob+=1
		if gh == "y":
			hprob+=1
		if hh == "y":
			hprob+=1
		print("Out of the 8 questions,",hprob,"were tested positive.")
		if hprob >= 5:
			print("You have a high chance of having a heat stroke. Go to your doctor immediately.")
		elif hprob <= 4 and hprob > 0:
			print("You have a slight chance of having a heat stroke. Go to your doctor to have an appointment on you about heat stroke.")
		elif hprob == 0:
			print("You don't have any chance of having a heat stroke soon. Woo-Hoo!")
		hmenu = input("Do you want to go back to the health menu?(y,n): ")
		if hmenu == "y":
			mainif()
		else:
			print("Thank you for using Vivan's health app. I hope you have a nice day.")
class Flu:
	def flu_symp():
		af = input("Do you have fever over 100° F?(y,n): ")
		bf = input("Do you have aching muscles, especially in your back, arms, and legs?(y,n): ")
		cf = input("Do you have chills and sweats?(y,n): ")
		df = input("Do you have unusual amounts of headaches?(y,n): ")
		ef = input("Do you have a dry persistent cough?(y,n): ")
		ff = input("Do you have fatigue and weakness?(y,n): ")
		gf = input("Do you have nasal congestion?(y,n): ")
		hf = input("Do you have sore throat?(y,n): ")
		fprob = 0
		if af == "y":
			fprob+=1
		if bf == "y":
			fprob+=1
		if cf == "y":
			fprob+=1
		if df == "y":
			fprob+=1
		if ef == "y":
			fprob+=1
		if ff == "y":
			fprob+=1
		if gf == "y":
			fprob+=1
		if hf == "y":
			fprob+=1
		print("Out of the 8 questions,",fprob,"were tested positive.")
		if fprob >= 5:
			print("You have a high chance of having the flu. Go to your doctor immediately.")
		elif fprob <= 4 and fprob > 0:
			print("You have a slight chance of having the flu. Go to your doctor to have an appointment on you about your flu.")
		elif fprob == 0:
			print("You don't have any chance of having the flu soon. Woo-Hoo!")
		fmenu = input("Do you want to go back to the health menu?(y,n): ")
		if fmenu == "y":
			mainif()
		else:
			print("Thank you for using Vivan's health app. I hope you have a nice day.")
#_______________________________________________________________________________________________________________________________________________________________________
#for lifestyle on health
class Aactivity:
	def walking():
		miles = float(input("How many miles did you walk today: "))
		weight = float(input("How much do you weigh?: "))
		TimesW =  float(input("How many times do you walk like this each day?"))
		GoalW = float(input("How many pounds do you want to reduce in order to reach your goal."))
		calories = (weight*.57)*miles
		lblost = calories/3500	
		weekW = lblost+TimesW
		print("Since you've walked",miles,"miles and weigh",weight,",you have burned",calories,"calories today.")
		print("You have lost",lblost,"pounds by walking today. Every week,you will burn",weekW,"pounds.")
		WWrepeat = input("Would you like to continue the app(y,n)?: ")
		if WWrepeat == "y":
			mainif()
		else:
			print("Have a nice day.")
	def running():
		milesR = float(input("How many miles did you run?: "))
		weightR = float(input("How much do you weigh?: "))
		TimesR = float(input("How many times do you run each week."))
		caloriesR = (weightR*.72)*milesR
		lblostR = caloriesR/3500
		weekR = lblostR*TimesR
		print("Since you ran",milesR,"miles and weigh",weightR,"pounds,you burned",caloriesR,"calories.")
		print("You have lost",lblostR,"pounds by running today. Every week you lose",weekR,"pounds.")
		RRrepeat = input("Would you like to continue the app(y,n)?: ")
		if RRrepeat == "y":
			mainif()
		else:
			print("Have a nice day.")
	def sporting():
		print("b.Basketball")
		print("s.Soccer")
		print("t.Tennis")
		print("v.Volleyball")
		print("f.Football")
		print("c.Cricket")
		print("w.wrestling")
		print("h.hockey")
		print("bs.baseball")
		print("g.gymnastics")
		h = input("Please choose: ")
		if h == "b":
			BBBweight = float(input("How much do you weigh?: "))
			BBBtime = float(input("How long did you play it(in minutes)? "))
			BBBkg = BBBweight/2.213
			BBBformula = (4.5*BBBkg*3.5)/200
			BBBtotal = BBBformula*BBBtime
			BBBlblost = BBBtotal/3500
			print("Since you played for",BBBtime,"minutes and weigh",BBBweight,"pounds, you burned",BBBtotal,"calories.")
			print("You lost",BBBlblost,"pounds")
			BBBrepeat = input("Would you like to continue the app(y,n)?: ")
			if BBBrepeat == "y":
				mainif()
			else:
				print("Have a nice day.")
		elif h == "s":
			CaOrCo = input("Are you playing competitive or practice right now(c,p)?")
			if CaOrCo == "c":
				Srweight = float(input("How much do you weigh?: "))
				Srtime = float(input("How long did you play it(in minutes)? "))
				Srkg = Srweight/2.213
				Srformula = (10*Srkg*3.5)/200
				Srtotal = Srformula*Srtime
				Srlblost = Srtotal/3500
				print("Since you played for",Srtime,"minutes and weigh",Srweight,"pounds, you burned",Srtotal,"calories.")
				print("You lost",Srlblost,"pounds")
			if CaOrCo == "p":
				Srpweight = float(input("How much do you weigh?: "))
				Srptime = float(input("How long did you play it(in minutes)? "))
				Srpkg = Srpweight/2.213
				Srpformula = (7*Srpkg*3.5)/200
				Srptotal = Srpformula*Srptime
				Srplblost = Srptotal/3500
				print("Since you played for",Srptime,"minutes and weigh",Srpweight,"pounds, you burned",Srptotal,"calories.")
				print("You lost",Srplblost,"pounds")
			CCrepeat = input("Would you like to continue the app(y,n)?: ")
			if CCrepeat == "y":
				mainif()
			else:
				print("Have a nice day.")
		elif h == "t":
			TordT = float(input("Are you playing a 1v1 or 2v2(1, or 2)?: "))
			if TordT == '1':
				Tweight = float(input("How much do you weigh?: "))
				Ttime = float(input("How long did you play it(in minutes)? "))
				Tkg = Tweight/2.213
				Tformula = (8*Tkg*3.5)/200
				Ttotal = Tformula*Ttime
				Tlblost = Ttotal/3500
				print("Since you played for",Ttime,"minutes and weigh",Tweight,"pounds, you burned",Ttotal,"calories.")
				print("You lost",Tlblost,"pounds")
			elif TordT == '2':
				DTweight = float(input("How much do you weigh?: "))
				DTtime = float(input("How long did you play it(in minutes)? "))
				DTkg = DTweight/2.213
				DTformula = (6*Tkg*3.5)/200
				DTtotal = DTformula*DTtime
				DTlblost = DTtotal/3500
				print("Since you played for",DTtime,"minutes and weigh",DTweight,"pounds, you burned",DTtotal,"calories.")
				print("You lost",DTlblost,"pounds")
			Trepeat = input("Would you like to continue the app(y,n)?: ")
			if Trepeat == "y":
				mainif()
			else:
				print("Have a nice day.")
		elif h == "v":
			Vweight = float(input("How much do you weigh?: "))
			Vtime = float(input("How long did you play it(in minutes)? "))
			Vkg = Vweight/2.213
			Vformula = (4*Vkg*3.5)/200
			Vtotal = Vformula*Vtime
			Vlblost = Vtotal/3500
			print("Since you played for",Vtime,"minutes and weigh",Vweight,"pounds, you burned",Vtotal,"calories.")
			print("You lost",Vlblost,"pounds")
			Vrepeat = input("Would you like to continue the app(y,n)?: ")
			if Vrepeat == "y":
				mainif()
			else:
				print("Have a nice day.")
		elif h == "f":
			FPordFC = input("Are you playing a competitive game or just practicing(c, or p)?: ")
			if FPordFC == "c":
				Fweight = float(input("How much do you weigh?: "))
				Ftime = float(input("How long did you play it(in minutes)? "))
				Fkg = Fweight/2.213
				Fformula = (8*Fkg*3.5)/200
				Ftotal = Fformula*Ftime
				Flblost = Ftotal/3500
				print("Since you played for",Ftime,"minutes and weigh",Fweight,"pounds, you burned",Ftotal,"calories.")
				print("You lost",Flblost,"pounds")
			elif FPordFC == "p":
				FPweight = float(input("How much do you weigh?: "))
				FPtime = float(input("How long did you play it(in minutes)? "))
				FPkg = FPweight/2.213
				FPformula = (2.5*Tkg*3.5)/200
				FPtotal = FPformula*FPtime
				FPlblost = FPtotal/3500
				print("Since you played for",FPtime,"minutes and weigh",FPweight,"pounds, you burned",FPtotal,"calories.")
				print("You lost",FPlblost,"pounds")
			FFrepeat = input("Would you like to continue the app(y,n)?: ")
			if FFrepeat == "y":
				mainif()
			else:
				print("Have a nice day.")
		elif h == "c":
			Cweight = float(input("How much do you weigh?: "))
			Ctime = float(input("For how long did you play it(in minutes)?: "))
			Ckg = Cweight/2.213
			Cformula = (4.8*Ckg*3.5)/200
			Ctotal = Cformula*Ctime
			Clblost = Ctotal/3500
			print("Since you weigh",Cweight,"pounds and played for",Ctime,"minutes,you burned",Ctotal,"calories.")
			print("You lost",Clblost,"pounds.")
			CCrepeat = input("Would you like to continue the app(y,n)?: ")
			if CCrepeat == "y":
				mainif()
			else:
				print("Have a nice day.")
		elif h == "w":
			Wweight = float(input("How much do you weigh?: "))
			Wtime = float(input("For how long did you play it(in minutes)?: "))
			Wkg = Wweight/2.213
			Wformula = (6*Wkg*3.5)/200
			Wtotal = Wformula*Wtime
			Wlblost = Wtotal/3500
			print("Since you weigh",Wweight,"pounds and played for",Wtime,"minutes,you burned",Wtotal,"calories.")
			print("You lost",Wlblost,"pounds.")
			WWErepeat = input("Would you like to continue the app(y,n)?: ")
			if WWErepeat == "y":
				mainif()
			else:
				print("Have a nice day.")
		elif h == "h":
			Hweight = input("How much do you weigh?: ")
			Htime = input("For how long did you play it(in minutes)?: ")
			Hkg = Hweight/2.213
			Hformula = (8*Hkg*3.5)/200
			Htotal = Hformula*Htime
			Hlblost = Htotal/3500
			print("Since you weigh",Hweight,"pounds and played for",Htime,"minutes,you burned",Htotal,"calories.")
			print("You lost",Hlblost,"pounds.")
			Hrepeat = input("Would you like to continue the app(y,n)?: ")
			if Hrepeat == "y":
				mainif()
			else:
				print("Have a nice day.")
		elif h == "bs":
			bsweight = float(input("How much do you weigh?: "))
			bstime = float(input("For how long did you play it(in minutes)?: "))
			bskg = bsweight/2.213
			bsformula = (5*bskg*3.5)/200
			bstotal = bsformula*bstime
			bslblost = bstotal/3500
			print("Since you weigh",bsweight,"pounds and played for",bstime,"minutes,you burned",bstotal,"calories.")
			print("You lost",bslblost,"pounds.")
			BSrepeat = input("Would you like to continue the app(y,n)?: ")
			if BSrepeat == "y":
				mainif()
			else:
				print("Have a nice day.")
		elif h == "g":
			gweight = float(input("How much do you weigh?: "))
			gtime = float(input("For how long did you play it(in minutes)?: "))
			gkg = gweight/2.213
			gformula = (3.8*gkg*3.5)/200
			gtotal = gformula*gtime
			glblost = gtotal/3500
			print("Since you weigh",gweight,"pounds and played for",gtime,"minutes,you burned",gtotal,"calories.")
			print("You lost",glblost,"pounds.")
			Grepeat = input("Would you like to continue the app(y,n)?: ")
			if Grepeat == "y":
				mainif()
			else:
				print("Have a nice day.")	
	def cycling():
		BCweight = float(input("How much do you weigh in pounds?: "))
		BCtime = float(input("For how long did you bike(in minutes)?: "))
		BCkg = BCweight/2.213
		BCformula = (5.8*BCkg*3.5)/200
		BCtotal = BCformula*BCtime
		BClblost = BCtotal/3500
		print("Since you weigh",BCweight,"pounds and cycled for",BCtime,"minutes, you lost",BCtotal,"calories.")
		print("You have lost",BClblost,"pounds.")
		CYrepeat = input("Would you like to continue the app(y,n)?: ")
		if CYrepeat == "y":
			mainif()
		else:
			print("Have a nice day.")
	def swimming():
		Sweight = float(input("How much do you weigh in pounds?: "))
		Stime = float(input("For how long did you swim(in minutes)?: "))
		Skg = Sweight/2.213
		Sformula = (6.0*Skg*3.5)/200
		Stotal = Sformula*Stime
		Slblost = Stotal/3500
		print("Since you weigh",Sweight,"pounds and cycled for",Stime,"minutes, you lost",Stotal,"calories.")
		print("You have lost",Slblost,"pounds.")
		Slrepeat = input("Would you like to continue the app(y,n)?: ")
		if repeat == "y":
			Slmainif()
		else:
			print("Have a nice day.")
	def stairss():
		RSorWS = input("Are you climbing and descending stairs at a fast pace or slow pace(f, or s)?: ")
		if RSorWS == "f":
			rweight = float(input("How much do you weigh?: "))
			rtime = float(input("How long did you play it(in minutes)? "))
			rkg = rweight/2.213
			rformula = (11.5*Fkg*3.5)/200
			rtotal = rformula*rtime
			rlblost = rtotal/3500
			print("Since you played for",rtime,"minutes and weigh",Fweight,"pounds, you burned",Ftotal,"calories.")
			print("You lost",Flblost,"pounds")
		elif RSorWS == "s":
			Wsweight = float(input("How much do you weigh?: "))
			Wstime = float(input("How long did you play it(in minutes)? "))
			Wskg = Wsweight/2.213
			Wsformula = (7.5*Wskg*3.5)/200
			Wstotal = Wsformula*Wstime
			Wslblost = Wstotal/3500
			print("Since you played for",Wstime,"minutes and weigh",Wsweight,"pounds, you burned",Wstotal,"calories.")
			print("You lost",Wslblost,"pounds")
		STrepeat = input("Would you like to continue the app(y,n)?: ")
		if STrepeat == "y":
			mainif()
		else:
			print("Have a nice day.")
	def skiingg():
		Skweight = float(input("How much do you weigh?: "))
		Sktime = float(input("How long did you play it(in minutes)? "))
		Skkg = Skweight/2.213
		Skformula = (7*Skkg*3.5)/200
		Sktotal = Skformula*Sktime
		Sklblost = Sktotal/3500
		print("Since you played for",Sktime,"minutes and weigh",Skweight,"pounds, you burned",Sktotal,"calories.")
		print("You lost",Sklblost,"pounds")
		SKrepeat = input("Would you like to continue the app(y,n)?: ")
		if SKrepeat == "y":
			mainif()
		else:
			print("Have a nice day.")
	def hikingg():
		HHweight = float(input("How much do you weigh?: "))
		HHtime = float(input("How long did you play it(in minutes)? "))
		HHkg = Skweight/2.213
		HHformula = (7*HHkg*3.5)/200
		HHtotal = HHformula*HHtime
		HHlblost = HHtotal/3500
		print("Since you played for",HHtime,"minutes and weigh",HHweight,"pounds, you burned",HHtotal,"calories.")
		print("You lost",HHlblost,"pounds.")
		Hrepeat = input("Would you like to continue the app(y,n)?: ")
		if Hrepeat == "y":
			mainif()
		else:
			print("Have a nice day.")
	def kayaking():
		Kweight = float(input("How much do you weigh?: "))
		Ktime = float(input("How long did you do it(in minutes)? "))
		Kkg = Kweight/2.213
		Kformula = (7*Kkg*3.5)/200
		Ktotal = Kformula*Ktime
		Klblost = Ktotal/3500
		print("Since you did kayaking for",Ktime,"minutes and weigh",Kweight,"pounds, you burned",Ktotal,"calories.")
		print("You lost",Klblost,"pounds.")
		Krepeat = input("Would you like to continue the app(y,n)?: ")
		if Krepeat == "y":
			mainif()
		else:
			print("Have a nice day.")
	def yoga():
		yweight = float(input("How much do you weigh?: "))
		ytime = float(input("How long did you do it(in minutes)? "))
		ykg = yweight/2.213
		yformula = (3.3*ykg*3.5)/200
		ytotal = yformula*ytime
		ylblost = ytotal/3500
		print("Since you did yoga for",ytime,"minutes and weigh",yweight,"pounds, you burned",ytotal,"calories.")
		print("You lost",ylblost,"pounds.")
		Yrepeat = input("Would you like to continue the app(y,n)?: ")
		if Yrepeat == "y":
			mainif()
		else:
			print("Have a nice day.")
class sleeping:
	def heightwhenawake():
		sleeptime = float(input("For how long do you sleep(in hours)?: "))
		sleepage = float(input("How old are you?: "))
		if sleepage > 0 and sleepage <= 18:
			sleepheight = sleeptime*.05555
			print("Since you are",sleepage,"years old, and slept for",sleeptime,"hours, you grew",sleepheight,"inches when you woke up.")
		else:
			print("You're too old to grow!!:P")
		HWArepeat = input("Would you like to continue the app(y,n)?: ")
		if HWArepeat == "y":
			mainif()
		else:
			print("Have a nice day.")
	def sleepcalorieloss():
		Slweight = float(input("How much do you weigh?: "))
		Sltime = float(input("How long did you sleep(in hours)? "))
		Sltimee = Sltime*60
		Slkg = Slweight/2.213
		Slformula = (0.94*Slkg*3.5)/200
		Sltotal = Slformula*Sltimee
		Sllblost = Sltotal/3500
		print("Since you slept for",Sltime,"hours and weigh",Slweight,"pounds, you burned",Sltotal,"calories.")
		print("You lost",Sllblost,"pounds")
		SCLrepeat = input("Would you like to continue the app(y,n)?: ")
		if SCLrepeat == "y":
			mainif()
		else:
			print("Have a nice day.")
	def sleepwait():
		slwait = float(input("How long do you sleep everyday?: "))
		slwaitt = 7-slwait
		if slwait > 7 and slwait <= 9:
			print("You can probably have a good night sleep. When you are sleeping, you will be able to heal and grow properly, and have enough energy restored.")
		else:
			print("You are going to have to sleep",slwaitt,"hours before you normally sleep.")
		SWrepeat = input("Would you like to continue the app(y,n)?: ")
		if SWrepeat == "y":
			mainif()
		else:
			print("Have a nice day.")
class Nutrition:
	def nutri():
		age = int(input("How old are you?: "))
		MorF = input("Are you a male or female(m,or f)?: ")
		if age > 1 and age <= 11:
			print("You will need from 1 to 1 1/2 cup of fruits, from 1 to 2 cups of veggies, from 3-5 ounces of grains, from 2-5 ounces of protein, and 2 to 2 1/2 cups of dairy.")
		elif age > 20 and age <= 64 and MorF == "f":
			print("You will need to enjoy but eat less food, drink more milks, make half your plate filled with fruits and vegetables, drink more water, eat whole grains more often, and cut back on fatty, oily, salty, and deep-fried foods by learning what are in foods, in order to be healthy.")
		elif age > 20 and age <= 64 and MorF == "m":
			print("You will need to eat many vegetables,fruits,whole grains,protein foods like beans,eggs,and lean meat(if you are not vegitarian), and eat and drink dairy like milks.Try to drink water every time you have a chance,instead of other drinks. Try to build habits that cut down eating food with lots of fat like a cookie. Learn about what different foods an beverages are made.")
		elif age > 11 and age <= 20 and MorF == "m":
			print("You will need to eat foods such as vegetables,fruits,whole grains,protein foods,and fat-free or low-dairy foods. If you're always hungry try eating most of your grains' foods with whole grain.Try drinking lots of water instead of sugered drinks. Skip foods with lots of fat like cookies. Learn what foods are made of to help you decide which foods are more healthy.")
		elif age > 11 and age <= 20 and MorF == "f":
			print("You will need to build strong bones by drinking lots of milks. Try to cut down on sweets like soda so you can maintain a healthy weight. Eat many foods with whole grain, since it will give you better protein. Try to eat vegetables with rich color because they have the vitamins and minerals that are essential for healthy growth. Check foods about what they are made of to help you decide what to eat to make you healthier.")
		elif age > 64 and age <= 100:
			print("You will need to drink plenty of sugar-free liquids like water often even if you don't feel that thirsty. Try to plan healthy meals everyday by learning about different foods and finding out which one is the healthiest for seniors. Try to recognize how much to eat,so you can control portion size. Try to vary your vegetables and their colors to brighten the plate. Find food that can help you eat with your teeth and gum like cooked fruits. Use herbs and spices to make the flavor taste better. Finally eat safely and ask your doctor about vitamins and supplements.")
		Nrepeat = input("Would you like to continue the app(y,n)?: ")
		if Nrepeat == "y":
			mainif()
		else:
			print("Have a nice day.")
class BodyControl:
	def MC():
		bcc = input("Are you feeling stressed, or unhappy about an event(y,n)?: ")
		if bcc == "y":
			physorment = input("Is this event a physhical activity(y,n): ")
			if physorment == "n":
				datew = int(input("In how many hours is the event?: "))
				if datew >= 24:
					print("Do meditation for every day and night for 30 minutes until the event, so you can concetrate more, get less bothered by distractions, have a better health, and have less stress for the event.")
				elif datew > 1 and datew < 24:
					print("Do meditation 2 hours before the event for 30 minutes, so you can concetrate more, get less bothered by distractions, have a better health, and have less stress for the event.")
				elif datew == 1:
					print("Do meditation 30 minutes before for 10 minutes, so you can concetrate more, get less bothered by distractions, have a better health, and have less stress for the event.")
			elif physorment == "y":
				dateww = int(input("In how many hours is the event?: "))
				if dateww >= 24:
					print("Do yoga for every day and night for 60 minutes until the event, so you can tone muscles, be more flexable, and have more mental smartness needed before the physical activity.")
				elif dateww > 1 and dateww < 24:
					print("Do meditation 2 hours before the event for 30 minutes, so you can tone muscles, be more flexable, and have more mental smartness needed before the physical activity.")
				elif dateww == 1:
					print("Do meditation 30 minutes before for 10 minutes, so you can tone muscles, be more flexable, and have more mental smartness needed before the physical activity.")
		bcrepeat = input("Would you like to continue the app(y,n)?: ")
		if bcrepeat == "y":
			mainif()
		else:
			print("Have a nice day.")
class Weightunderstanding:
	def bmi():
		weightt = float(input("How much do you weigh(in lbs)?: "))
		height = float(input("How tall are you(in inches)?: "))
		heightplus = height*height
		formulaBMI = (weightt/heightplus)*703
		if formulaBMI < 18.5:
			print("You are underweight because your bmi is",formulaBMI,".")
		elif formulaBMI >= 18.5 and formulaBMI <= 24.9:
			print("You are average because your bmi is",formulaBMI,".")
		elif formulaBMI > 24.9 and formulaBMI <= 29.9:
			print("You are overweight because your bmi is",formulaBMI,".")
		elif formulaBMI > 29.9:
			print("You are OBESE because your bmi is",formulaBMI,".")
	def bmiprime():
		restofW = 25
		sea = 23
		SWA = input("Do you live in Southeast Asia(y,n)?: ")
		heightt = float(input("How tall are you(in inches)?: "))
		weighttt = float(input("How much do you weigh(y,n)?: "))
		if SWA == "n":
			heightt_t = heightt*heightt
			formulaBmiP = (weighttt/heightt_t*703)/25
			if formulaBmiP > 0.63 and formulaBmiP < 75:
				print("You are underweight because your bmi prime is",formulaBmiP,".")
			elif formulaBmiP > 0.73 and formulaBmiP <= 1:
				print("You have a healthy weight because your bmi prime is",formulaBmiP,".")
			elif formulaBmiP > 0.99 and formulaBmiP <= 1.2:
				print("You are overweight because your bmi prime is",formulaBmiP,".")
		if SWA == "y":
			heightt_t = heightt*heightt
			formulaBmiP = (weighttt/heightt_t*703)/23
			if formulaBmiP > 0.63 and formulaBmiP < 75:
				print("You are underweight because your bmi prime is",formulaBmiP,".")
			elif formulaBmiP > 0.73 and formulaBmiP <= 1:
				print("You have a healthy weight because your bmi prime is",formulaBmiP,".")
			elif formulaBmiP > 0.99 and formulaBmiP <= 1.2:
				print("You are overweight because your bmi prime is",formulaBmiP,".")		

Ccounter = 0
Dcounter = 0
HAcounter = 0
PNcounter = 0
BCcounter = 0
Acounter = 0
Tcounter = 0
ALZcounter = 0
CHOLcounter = 0
DIcounter = 0
DEHcounter = 0
HScounter = 0
Fcounter = 0

class MedReport:
	def check():
		print("Please use the report before using this part.")
		print("1.Cancer")
		print("2.Diabetes")
		print("3.Heart attack")
		print("4.Pneumonia")
		print("5.Bronchitas")
		print("6.Asthma")
		print("7.Turberculosis")
		print("8.Alzheimer's")
		print("9.Cholesterol")
		print("10.Diarrhea")
		print("11.Dehydration")
		print("12.Heat stroke")
		print("13.Flu")
		lll = input("Please choose the sickness said that you have on the medical report or symptoms search: ")
		if lll == '1':
			print("Go to the doctor soon to find out what to do with your cancer.")
		elif lll == '2':
			print("To cure it using home remedies, do the following: have healthy eating by centering your diet on more fruits,vegetables,lean proteins,whole grains,and sugar once in a while if its part of your meal plan, and have lots of physical activity by aiming for at least 30 minutes total and gradually move on.")
		elif lll == '3':
			print("Go meet your doctor to see what to do with your chance of having a heart attack.")
		elif lll == '4':
			print("Go to your doctor in some time and find the antibiotics the doctor gives you. At home, get cough medicine and get fever reducers/pain relievers like Tylenol.")
		elif lll == '5':
			print("To cure yourself using home remedies, do the following: avoid lung irritants that makes the air polluted, use a clean humidifier to make warm,moist air,and consider a face mask outside.")
		elif lll == '6':
			print("Go to the doctor soon to find out what to do if you have asthma.")
		elif lll == '7':
			print("Go to the doctor soon to find out what to do if you have turberculosis.")
		elif lll == '8':
			print("Go to the doctor soon to find out what to do if you have alzheimers.")
		elif lll == '9':
			print("To cure yourself using home remedies, do the following: use statins to help control the cholesterol, use bile-acid binding resins to lower the level of cholesterol, use cholesterol absorption inhibitors to help reduce blood cholesterol, and have injectable medicines.")
		elif lll == '10':
			print("To cure it using home remedies, do the following: drink plenty of clear liquids like water, do not drink alchohol or caffeine, consider taking probiotics like yogurt, and avoid certain foods such as dairy or fatty foods.")
		elif lll == '11':
			print("To cure it using home remedies, do the following: increase your water intake by alot, drink coconut water, eat bananas, watery fruits and vegetables, and eat yogurt.")
		elif lll == '12':
			print(" To cure it using home remedies, do the following: immerse yourself in cold water like a bath of cold water, use evaporation cooling techniques, pack yourself with ice and cooling blankets, and give yourself medications to stop shivering.")
		elif lll == '13':
			print("To cure it using home remedies, do the following: drink lots of fluids like water, sip some soup, do not exercise at all, and try using nasal irrigation.")
		CCrepeat = input("Would you like to continue the app(y,n)?: ")
		if CCrepeat == "y":
			mainif()
		else:
			print("Have a nice day.")
	def MDRT():
		global Ccounter
		global Dcounter
		global HAcounter
		global PNcounter
		global BCcounter
		global Acounter
		global Tcounter
		global ALZcounter
		global CHOLcounter
		global DIcounter
		global DEHcounter
		global HScounter
		global Fcounter

		os.system('clear')
		mrt = int(input("""
			
			Throat/Mouth/Breathing

			1. hoarseness 6. persistent lumps or swollen glands 
			7. increased thirst 13. frequent dry mouths 16. shortness of breath
			22. phlegm-producing cough 24. cough with clear, yellow, or green sputum 
			25. wheezing 29. whistling or wheezing sound when sleeping 
			30. coughing that lasts three or more weeks 31. cough blood 44. cough with a dry mouth
			55. rapid, shallow breathing  

			Skin

			2. obvious change in wart or a mole 48. dry skin 51. red,hot and dry skin

			Pain

			15. chest pain 20. pain when breath or cough
			28. trouble sleeping caused by breath,coughing,or wheezing
			27. chest tightness 33. chills 39. pain in the neck,jaw, or back
			52.muscle weakness or cramps 54. rapid heartbeat

			Digestion

			3. unexplained weight loss 4. indigestion/difficulty swallowing
			8. increased hunger especially after eating 
			9. unexplained weight loss even though eating 42. stomach ache 53. vomit

			Excretion

			5. blood in urine 12. frequent urinating or urine infections 
			17. cold sweat 23. fever, sweating, and chills 26. runny nose
			32. night sweats 40.numbness or coldness in excremities	41. liquid doo-doo
			43. bloody poo 46. decreased urine output 47. yellow urine 

			Head/Mental

			10. constant headaches 11. fatigue 14. blurred vision
			18. nausea 19. lightheadedness 21. confusion in mental awareness
			34. memory loss 35. challenges in planning/solving problems
			36. difficulty completing familiar tasks 37. confusion with time/place
			38. trouble understanding images and relationships   
			45. unusually become tired or sleepy 49. dizziness 50. no sweat despite heat   
				"""))
		
		if mrt==0:
	#_____________________________________________________________________________________________________________________________________________		
			if Ccounter > 0:
				if (Ccounter/6) > (2/3):
					sys.stdout.write(BOLD)
					sys.stdout.write(RED)
					print('Out of all of the symptoms for cancer, you tested positive for cancer in', round((Ccounter/6)*100, 2), '%% of them.')
					sys.stdout.write(RESET)
				elif ((Ccounter/6) > 1/3) and ((Ccounter/6) <= 2/3):
					sys.stdout.write(BOLD)
					print('Out of all of the symptoms for cancer, you tested positive for cancer in', round((Ccounter/6)*100, 2), '%% of them.')
					sys.stdout.write(RESET)
				elif ((Ccounter/6) > 0) and ((Ccounter/6) <= 1/3):
					sys.stdout.write(BOLD)
					print('Out of all of the symptoms for cancer, you tested positive for cancer in', round((Ccounter/6)*100, 2), '%% of them.')
					sys.stdout.write(RESET)
			elif Ccounter == 0:
				sys.stdout.write(BOLD)
				sys.stdout.write(GREEN)
				print('Out of all of the symptoms for cancer, you tested positive for cancer in', round((Ccounter/6)*100, 2), '%% of them.')
				sys.stdout.write(RESET)
			if Dcounter > 0:
				if (Dcounter/8) > (2/3):
					sys.stdout.write(BOLD)
					sys.stdout.write(RED)
					print('Out of all of the symptoms for diabetes, you tested positive for diabetes in', round((Dcounter/8)*100, 2), '%% of them. ')
					sys.stdout.write(RESET)
				elif ((Dcounter/8) > 1/3) and ((Dcounter/8) <= 2/3):
					sys.stdout.write(BOLD)
					print('Out of all of the symptoms for diabetes, you tested positive for diabetes in', round((Dcounter/8)*100, 2), '%% of them. ')
					sys.stdout.write(RESET)
				elif ((Dcounter/8) > 0) and ((Dcounter/8) <= 1/3):
					sys.stdout.write(BOLD)
					print('Out of all of the symptoms for diabetes, you tested positive for diabetes in', round((Dcounter/8)*100, 2), '%% of them.')
					sys.stdout.write(RESET)
			elif Dcounter == 0:
				sys.stdout.write(BOLD)
				sys.stdout.write(GREEN)
				print('Out of all of the symptoms for diabetes, you tested positive for diabetes in', round((Dcounter/8)*100, 2), '%% of them.')
				sys.stdout.write(RESET)
			if HAcounter > 0:
				if (HAcounter/5) > (2/3):
					sys.stdout.write(BOLD)
					sys.stdout.write(RED)
					print('Out of all of the symptoms for heart attack, you tested positive for heart attack in', round((HAcounter/5)*100, 2), '%% of them.')
					sys.stdout.write(RESET)
				elif ((HAcounter/5) > 1/3) and ((HAcounter/5) <= 2/3):
					sys.stdout.write(BOLD)
					print('Out of all of the symptoms for heart attack, you tested positive for heart attack in', round((HAcounter/5)*100, 2), '%% of them.')
					sys.stdout.write(RESET)
				elif ((HAcounter/5) > 0) and ((HAcounter/5) <= 1/3):
					sys.stdout.write(BOLD)
					print('Out of all of the symptoms for heart attack, you tested positive for heart attack in', round((HAcounter/5)*100, 2), '%% of them.')
					sys.stdout.write(RESET)
			elif HAcounter == 0:
				sys.stdout.write(BOLD)
				sys.stdout.write(GREEN)
				print('Out of all of the symptoms for heart attack, you tested positive for heart attack in', round((HAcounter/5)*100, 2), '%% of them.')
				sys.stdout.write(RESET)
			if PNcounter > 0:
				if (PNcounter/6) > (2/3):
					sys.stdout.write(BOLD)
					sys.stdout.write(RED)
					print('Out of all of the symptoms for pneumonia, you tested positive for pneumonia in', round((PNcounter/6)*100, 2), '%% of them.')
					sys.stdout.write(RESET)
				elif ((PNcounter/6) > 1/3) and ((PNcounter/6) <= 2/3):
					sys.stdout.write(BOLD)
					print('Out of all of the symptoms for pneumonia, you tested positive for pneumonia in', round((PNcounter/6)*100, 2), '%% of them.')
					sys.stdout.write(RESET)
				elif ((PNcounter/6) > 0) and ((PNcounter/6) <= 1/3):
					sys.stdout.write(BOLD)
					print('Out of all of the symptoms for pneumonia, you tested positive for pneumonia in', round((PNcounter/6)*100, 2), '%% of them.')
					sys.stdout.write(RESET)
			elif PNcounter == 0:
				sys.stdout.write(BOLD)
				sys.stdout.write(GREEN)
				print('Out of all of the symptoms for pneumonia, you tested positive for pneumonia in', round((PNcounter/6)*100, 2), '%% of them.')
				sys.stdout.write(RESET)
			if BCcounter > 0:
				if (BCcounter/6) > (2/3):
					sys.stdout.write(BOLD)
					sys.stdout.write(RED)
					print('Out of all of the symptoms for bronchitis, you tested positive for bronchitis in', round((BCcounter/6)*100, 2), '%% of them.')
					sys.stdout.write(RESET)
				elif ((BCcounter/6) > 1/3) and ((BCcounter/6) <= 2/3):
					sys.stdout.write(BOLD)
					print('Out of all of the symptoms for bronchitis, you tested positive for bronchitis in', round((BCcounter/6)*100, 2), '%% of them.')
					sys.stdout.write(RESET)
				elif ((BCcounter/6) > 0) and ((BCcounter/6) <= 1/3):
					sys.stdout.write(BOLD)
					print('Out of all of the symptoms for bronchitis, you tested positive for bronchitis in', round((BCcounter/6)*100, 2), '%% of them.')
					sys.stdout.write(RESET)
			elif BCcounter == 0:
				sys.stdout.write(BOLD)
				sys.stdout.write(GREEN)
				print('Out of all of the symptoms for bronchitis, you tested positive for bronchitis in', round((BCcounter/6)*100, 2), '%% of them.')
				sys.stdout.write(RESET)
			if Acounter > 0:
				if (Acounter/4) > (2/3):
					sys.stdout.write(BOLD)
					sys.stdout.write(RED)
					print('Out of all of the symptoms for asthma, you tested positive for asthma in', round((Acounter/4)*100, 2), '%% of them.')
					sys.stdout.write(RESET)
				elif ((Acounter/4) > 1/3) and ((Acounter/4) <= 2/3):
					sys.stdout.write(BOLD)
					print('Out of all of the symptoms for asthma, you tested positive for asthma in', round((Acounter/4)*100, 2), '%% of them.')
					sys.stdout.write(RESET)
				elif ((Acounter/4) > 0) and ((Acounter/4) <= 1/3):
					sys.stdout.write(BOLD)
					print('Out of all of the symptoms for asthma, you tested positive for asthma in', round((Acounter/4)*100, 2), '%% of them.')
					sys.stdout.write(RESET)
			elif Acounter == 0:
				sys.stdout.write(BOLD)
				sys.stdout.write(GREEN)
				print('Out of all of the symptoms for asthma, you tested positive for asthma in', round((Acounter/4)*100, 2), '%% of them.')
				sys.stdout.write(RESET)
			if Tcounter > 0:
				if (Tcounter/7) > (2/3):
					sys.stdout.write(BOLD)
					sys.stdout.write(RED)
					print('Out of all of the symptoms for turbeloscis, you tested positive for turbeloscis in', round((Tcounter/7)*100, 2), '%% of them.')
					sys.stdout.write(RESET)
				elif ((Tcounter/7) > 1/3) and ((Tcounter/7) <= 2/3):
					sys.stdout.write(BOLD)
					print('Out of all of the symptoms for turbeloscis, you tested positive for turbeloscis in', round((Tcounter/7)*100, 2), '%% of them.')
					sys.stdout.write(RESET)
				elif ((Tcounter/7) > 0) and ((Tcounter/7) <= 1/3):
					sys.stdout.write(BOLD)
					print('Out of all of the symptoms for turbeloscis, you tested positive for turbeloscis in', round((Tcounter/7)*100, 2), '%% of them.')
					sys.stdout.write(RESET)
			elif Tcounter == 0:
				sys.stdout.write(BOLD)
				sys.stdout.write(GREEN)
				print('Out of all of the symptoms for turbeloscis, you tested positive for turbeloscis in', round((Tcounter/7)*100, 2), '%% of them.')
				sys.stdout.write(RESET)
			if ALZcounter > 0:
				if (ALZcounter/5) > (2/3):
					sys.stdout.write(BOLD)
					sys.stdout.write(RED)
					print('Out of all of the symptoms for alzheimers, you tested positive for alzheimers in', round((ALZcounter/5)*100, 2), '%% of them.')
					sys.stdout.write(RESET)
				elif ((ALZcounter/5) > 1/3) and ((ALZcounter/5) <= 2/3):
					sys.stdout.write(BOLD)
					print('Out of all of the symptoms for alzheimers, you tested positive for alzheimers in', round((ALZcounter/5)*100, 2), '%% of them.')
					sys.stdout.write(RESET)
				elif ((ALZcounter/5) > 0) and ((ALZcounter/5) <= 1/3):
					sys.stdout.write(BOLD)
					print('Out of all of the symptoms for alzheimers, you tested positive for alzheimers in', round((ALZcounter/5)*100, 2), '%% of them.')
					sys.stdout.write(RESET)
			elif ALZcounter == 0:
				sys.stdout.write(BOLD)
				sys.stdout.write(GREEN)
				print('Out of all of the symptoms for alzheimers, you tested positive for alzheimers in', round((ALZcounter/5)*100, 2), '%% of them.')
				sys.stdout.write(RESET)
			if CHOLcounter > 0:
				if (CHOLcounter/6) > (2/3):
					sys.stdout.write(BOLD)
					sys.stdout.write(RED)
					print('Out of all of the symptoms for cholestrol, you tested positive for cholestrol in', round((CHOLcounter/6)*100, 2), '%% of them.')
					sys.stdout.write(RESET)
				elif ((CHOLcounter/6) > 1/3) and ((CHOLcounter/6) <= 2/3):
					sys.stdout.write(BOLD)
					print('Out of all of the symptoms for cholestrol, you tested positive for cholestrol in', round((CHOLcounter/6)*100, 2), '%% of them.')
					sys.stdout.write(RESET)
				elif ((CHOLcounter/6) > 0) and ((CHOLcounter/6) <= 1/3):
					sys.stdout.write(BOLD)
					print('Out of all of the symptoms for cholestrol, you tested positive for cholestrol in', round((CHOLcounter/6)*100, 2), '%% of them.')
					sys.stdout.write(RESET)
			elif CHOLcounter == 0:
				sys.stdout.write(BOLD)
				sys.stdout.write(GREEN)
				print('Out of all of the symptoms for cholestrol, you tested positive for cholestrol in', round((CHOLcounter/6)*100, 2), '%% of them.')
				sys.stdout.write(RESET)
			if DIcounter > 0:
				if (DIcounter/4) > (2/3):
					sys.stdout.write(BOLD)
					sys.stdout.write(RED)
					print('Out of all of the symptoms for diarrhea, you tested positive for diarrhea in', round((DIcounter/4)*100, 2), '%% of them.')
					sys.stdout.write(RESET)
				elif ((DIcounter/4) > 1/3) and ((DIcounter/4) <= 2/3):
					sys.stdout.write(BOLD)
					print('Out of all of the symptoms for diarrhea, you tested positive for diarrhea in', round((DIcounter/4)*100, 2), '%% of them.')
					sys.stdout.write(RESET)
				elif ((DIcounter/4) > 0) and ((DIcounter/4) <= 1/3):
					sys.stdout.write(BOLD)
					print('Out of all of the symptoms for diarrhea, you tested positive for diarrhea in', round((DIcounter/4)*100, 2), '%% of them.')
					sys.stdout.write(RESET)
			elif DIcounter == 0:
				sys.stdout.write(BOLD)
				sys.stdout.write(GREEN)
				print('Out of all of the symptoms for diarrhea, you tested positive for diarrhea in', round((DIcounter/4)*100, 2), '%% of them.')
				sys.stdout.write(RESET)
			if DEHcounter > 0:
				if (DEHcounter/7) > (2/3):
					sys.stdout.write(BOLD)
					sys.stdout.write(RED)
					print('Out of all of the symptoms for dehydration, you tested positive for dehydration in', round((DEHcounter/7)*100, 2), '%% of them.')
					sys.stdout.write(RESET)
				elif ((DEHcounter/7) > 1/3) and ((DEHcounter/7) <= 2/3):
					sys.stdout.write(BOLD)
					print('Out of all of the symptoms for dehydration, you tested positive for dehydration in', round((DEHcounter/7)*100, 2), '%% of them.')
					sys.stdout.write(RESET)
				elif ((DEHcounter/7) > 0) and ((DEHcounter/7) <= 1/3):
					sys.stdout.write(BOLD)
					print('Out of all of the symptoms for dehydration, you tested positive for dehydration in', round((DEHcounter/7)*100, 2), '%% of them.')
					sys.stdout.write(RESET)
			elif DEHcounter == 0:
				sys.stdout.write(BOLD)
				sys.stdout.write(GREEN)
				print('Out of all of the symptoms for dehydration, you tested positive for dehydration in', round((DEHcounter/7)*100, 2), '%% of them.')
				sys.stdout.write(RESET)
			if HScounter > 0:
				if (HScounter/9) > (2/3):
					sys.stdout.write(BOLD)
					sys.stdout.write(RED)
					print('Out of all of the symptoms for heat stroke, you tested positive for heat stroke in', round((HScounter/9)*100, 2), '%% of them.')
					sys.stdout.write(RESET)
				elif ((HScounter/9) > 1/3) and ((HScounter/9) <= 2/3):
					sys.stdout.write(BOLD)
					print('Out of all of the symptoms for heat stroke, you tested positive for heat stroke in', round((HScounter/9)*100, 2), '%% of them.')
					sys.stdout.write(RESET)
				elif ((HScounter/9) > 0) and ((HScounter/9) <= 1/3):
					sys.stdout.write(BOLD)
					print('Out of all of the symptoms for heat stroke, you tested positive for heat stroke in', round((HScounter/9)*100, 2), '%% of them.')
					sys.stdout.write(RESET)
			elif HScounter == 0:
				sys.stdout.write(BOLD)
				sys.stdout.write(GREEN)
				print('Out of all of the symptoms for heat stroke, you tested positive for heat stroke in', round((HScounter/9)*100, 2), '%% of them.')
				sys.stdout.write(RESET)
			if Fcounter > 0:
				if (Fcounter/4) > (2/3):
					sys.stdout.write(BOLD)
					sys.stdout.write(RED)
					print('Out of all of the symptoms for flu, you tested positive for flu in', round((Fcounter/4)*100, 2), '%% of them.')
					sys.stdout.write(RESET)
				elif ((Fcounter/4) > 1/3) and ((Fcounter/4) <= 2/3):
					sys.stdout.write(BOLD)
					print('Out of all of the symptoms for flu, you tested positive for flu in', round((Fcounter/4)*100, 2), '%% of them.')
					sys.stdout.write(RESET)
				elif ((Fcounter/4) > 0) and ((Fcounter/4) <= 1/3):
					sys.stdout.write(BOLD)
					print('Out of all of the symptoms for flu, you tested positive for flu in', round((Fcounter/4)*100, 2), '%% of them.')
					sys.stdout.write(RESET)
			elif Fcounter == 0:
				sys.stdout.write(BOLD)
				sys.stdout.write(GREEN)
				print('Out of all of the symptoms for flu, you tested positive for flu in', round((Fcounter/4)*100, 2), '%% of them.')
				sys.stdout.write(RESET)

#_____________________________________________________________________________________________________________________________________________

		elif mrt==15:
			PNcounter += 1
			Tcounter += 1
			CHOLcounter += 1
			HAcounter += 1
			MedReport.MDRT()
		elif mrt == 3:
			Ccounter += 1
			Dcounter += 1
			MedReport.MDRT()
		elif mrt==7:
			DEHcounter += 1
			Dcounter += 1
			MedReport.MDRT()
		elif mrt == 10:
			HScounter += 1
			MedReport.MDRT()
		elif mrt==39:
			Fcounter += 1
			CHOLcounter += 1
			MedReport.MDRT()
		elif mrt==18:
			HAcounter += 1
			CHOLcounter += 1
			HScounter += 1
			MedReport.MDRT()
		elif mrt == 19:
			HAcounter += 1
			HScounter += 1
			MedReport.MDRT()
		elif mrt == 11:
			PNcounter += 1
			Dcounter += 1
			BCcounter += 1
			CHOLcounter += 1
			Tcounter += 1
			Fcounter += 1
			MedReport.MDRT()
		elif mrt==16:
			Acounter += 1
			HAcounter += 1
			BCcounter += 1
			CHOLcounter += 1
			MedReport.MDRT()
		elif mrt==23:
			PNcounter += 1
			BCcounter += 1
			Tcounter += 1
			DIcounter += 1
			Fcounter += 1
			MedReport.MDRT()
		elif mrt==33:
			Tcounter += 1
			Fcounter += 1
			MedReport.MDRT()
		elif (mrt==1) or (mrt==2) or (mrt==4) or (mrt==5) or (mrt==6):
			Ccounter += 1
			MedReport.MDRT()
		elif (mrt==8) or (mrt==9) or (mrt==12) or (mrt==13) or (mrt==14):
			Dcounter += 1
			MedReport.MDRT()
		elif (mrt==17):
			HAcounter += 1
			MedReport.MDRT()
		elif (mrt==20) or (mrt==21) or (mrt==22):
			PNcounter += 1
			MedReport.MDRT()
		elif (mrt==24) or (mrt==25) or (mrt==26):
			BCcounter += 1
			MedReport.MDRT()
		elif (mrt==27) or (mrt==28) or (mrt==29):
			Acounter += 1
			MedReport.MDRT()
		elif (mrt==30) or (mrt==31) or (mrt==32):
			Tcounter += 1
			MedReport.MDRT()
		elif (mrt==34) or (mrt==35) or (mrt==36) or (mrt==37) or (mrt==38):
			ALZcounter += 1
			MedReport.MDRT()
		elif (mrt==40):
			CHOLcounter += 1
			MedReport.MDRT()
		elif (mrt==41) or (mrt==42) or (mrt==43):
			DIcounter += 1
			MedReport.MDRT()
		elif (mrt==44) or (mrt==45) or (mrt==46) or (mrt==47) or (mrt==48) or (mrt==49):
			DEHcounter += 1
			MedReport.MDRT()
		elif (mrt==50) or (mrt==51) or (mrt==52) or (mrt==53) or (mrt==54) or (mrt==55):
			HScounter += 1
			MedReport.MDRT()
			repeat = input("Would you like to continue the app(y,n)?: ")
			if repeat == "y":
				mainif()
			else:
				print("Have a nice day.")
class tall:
	def heightdeterming():
		Mheight = int(input("How tall is your mother in inches?: "))
		Fheight = int(input("How tall is your dad in inches?: "))
		GorB = input("Are you male or female(m, or f)?: ")
		if GorB == "m":
			formulaM = (Mheight+Fheight+5)/2
			if formulaM >= 67:
				print("You probably will be taller than the average height because your height was predicted to be ",formulaM,"inches.")
			if formulaM < 67:
				print("You probably will be shorter than the average height because your height was predicted to be ",formulaM,"inches.")
		elif Gorb == "f":
			formulaG = (Mheight+Fheight-5)/2
			if formulaG >= 63:
				print("You probably will be taller than the average height because your height was predicted to be ",formulaG,"inches.")
			if formulaG < 63:
				print("You probably will be shorter than the average height because your height was predicted to be ",formulaG,"inches.")
		HDrepeat = input("Would you like to continue the app(y,n)?: ")
		if HDrepeat == "y":
			mainif()
		else:
			print("Have a nice day.")
	def babyHeightP():
		gorb = input("Is your baby a girl or boy(g, or b)?: ")
		if gorb == "b":
			heightwhentwo = int(input("How tall was/is your baby when he was 2 years ol?: "))
			form = heightwhentwo*2
			print("your baby is predicted to be",form,"inches when he is an adult.")
		elif gorb == "g":
			heightwhen18m = int(input("How tall was your baby when she was 18 months?: "))
			formG = heightwhen18m*2
			print("Your baby is predicted to be",formG,"inches when she is an adult.")
		BHPrepeat = input("Would you like to continue the app(y,n)?: ")
		if BHPrepeat == "y":
			mainif()
		else:
			print("Have a nice day.")
#-------------------------------------------needs----------------------------------------------------------------------------------------------------------------------------
#Main if statement
def mainif():
	print("0.Quit App")
	print("1.For checking symptoms of different diseases and threats to your body.")
	print("2.For finding your activity and physical and mental health.")
	print("3.Medical Report")
	print("4.Sickness curer/Health helper")
	print("	   - Try to use after using .1. or .3.")

	mm = input("Please choose: ")
	if mm == '1':	
		print("1.Cancer")
		print("2.Diabetes")
		print("3.Heart attack")
		print("4.Pneumonia")
		print("5.Bronchitas chitas")
		print("6.Asthma")
		print("7.Turberculosis")
		print("8.Alzheimer's")
		print("9.Cholesterol")
		print("10.Diarrhea")
		print("11.Dehydration")
		print("12.Heat stroke")
		print("13.Flu")
		m = input("Please choose: ")
		if m == '1':
			Cancer.cancertest()
		elif m == '2':
			Diabetes.diabetessyptoms()
		elif m == '3':
			HeartAttack.Heartattacksymptoms()
		elif m == '4':
			pneumonia.pneumoniatest()
		elif m == '5':
			bronchitasChitas.Bc()
		elif m == '6':
			Asthma.asthmatest()
		elif m == '7':
			Turbeloscis.Turbotest()
		elif m == '8':
			Alzheimerss.alz_test()
		elif m == '9':
			Cholesterol.cholestroltest()
		elif m == '10':
			Diarrheaa.diarrheatest()
		elif m == '11':
			Dehydration.dehy()
		elif m == '12':
			HeatStroke.HS()
		elif m == '13':
			Flu.flu_symp()
	elif mm == '2':
		print("1.Activity")
		print("2.Sleeping")
		print("3.Nutrition")
		print("4.Body control")
		print("5.Height prediction")
		print("6.weight control learner")
		mmm = input("Please choose: ")
		if mmm == '1':
			print("1.Activity of walking.")
			print("2.Activity of running")
			print("3.Sports")
			print("4.Activity of cycling")
			print("5.Activity of swimming")
			print("6.Activity of stairs")
			print("7.Activity of skiing")
			print("8.Activity of hiking")
			print("9.Activity of kayaking")
			print("10.Activity of meditation")
			print("11.ACtivity of yoga")
			aaa = input("Please choose: ")
			if aaa == '1':
				Aactivity.walking()
			if aaa == '2':
				Aactivity.running()
			if aaa == '3':
				Aactivity.sporting()
			if aaa == '4':
				Aactivity.cycling()
			if aaa == '5':
				Aactivity.swimming()
			if aaa == '6':
				Aactivity.stairss()
			if aaa == '7':
				Aactivity.skiingg()
			if aaa == '8':
				Aactivity.hikingg()
			if aaa == '9':
				Aactivity.kayaking()
			if aaa == '10':
				Aactivity.meditation()
			if aaa == '11':
				Aactivity.yoga()
		elif mmm == '2':
			print("1.Sleep growth")
			print("2.Sleep start and stop")
			print("3.Sleep calorie loss")
			sss = input("Please choose: ")
			if sss == '1':
				sleeping.heightwhenawake()
			elif sss == '2':
				sleeping.sleepwait()
			elif sss == '3':
				sleeping.sleepcalorieloss()

		elif mmm == '3':
			Nutrition.nutri()
		elif mmm == '4':
			BodyControl.MC()
		elif mmm == '5':
			print("1.Predicted adult height for children")
			print("2.Predicted adult height for babies")
			hhh = input("Please choose: ")
			if hhh == '1':
				tall.heightdeterming()
			elif hh == '2':
				tall.babyHeightP()
		elif mmm == '6':
			print("1.BMI")
			print("2.BMI Prime")
			wwww = input("please choose?: ")
			if wwww == '1':
				Weightunderstanding.bmi()
			if wwww == '2':
				Weightunderstanding.bmiprime()

	elif mm == '3':
		MedReport.MDRT()
	elif mm == '4':
		MedReport.check()
	elif mm == '0':
		print("Thank you for using the health app, I hope we meet in the future! - Vivan and Veer Doshi")
mainif()