import joblib

model = joblib.load("model.pkl")

vize = float(input("Vize notu: "))
katilim = float(input("Katılım: "))

prediction = model.predict([[vize, katilim]])
final_not = prediction[0]

def harf_notu(score):
    if score >= 90 : return "AA"
    elif score >= 80 : return "BA"
    elif score >= 70 : return "BB"
    elif score >= 60 : return "CB"
    elif score >= 50 : return "CC"
    else : return "FF"

print("\n-----Sonuç-----")
print("Tahmin edilen final notu:", round(final_not, 2))
print("Harf Notu: ", harf_notu(final_not))
