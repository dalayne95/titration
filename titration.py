def calculate_titration(molarity_of_titrant, volume_of_titrant, volume_of_analyte):
	molarity_of_analyte = (molarity_of_titrant * volume_of_titrant) / volume_of_analyte
	return molarity_of_analyte


molarity_titrant = input("enter molarity of titrant: ")
volume_titrant = input("enter volume of titrant: ")
volume_analyte = input("enter volume of analyte: ")

molarity_analyte = calculate_titration(float(molarity_titrant), float(volume_titrant), float(volume_analyte))

print("molarity analyte: " + str(molarity_analyte))