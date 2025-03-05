from drugprescription import sentimentanalyzer
from drugprescription.models import MedicineModel, UserModel, ReviewModel

def getMedicinesByStore(username):
    medicines = []
    for medicine in MedicineModel.objects.all():
        if username in medicine.username:
            medicines.append(medicine)
    return medicines

def findMedicineByName(location,name):
    medicines = {}
    for medicine in MedicineModel.objects.all():
        if name.lower() in medicine.name.lower():
            store = UserModel.objects.get(username=medicine.username)
            address = store.address

            if location.lower() in address.lower():
                medicine.store = store.name
                medicine.address = store.address
                positive=0

                for review in ReviewModel.objects.filter(medicine=medicine.id):

                    result=sentimentanalyzer.getCommentSentiment(review.review)

                    if result=='positive':
                        positive=positive+1

                medicines.update({medicine:positive})

    print("Before",medicines)

    # Sorting the dictionary by its values in descending order
    sorted_data = dict(sorted(medicines.items(), key=lambda item: item[1], reverse=True))

    print("After", sorted_data)

    return sorted_data.keys()


def searchMedicineBySymptoms(location,symptoms):
    medicines = []
    for medicine in MedicineModel.objects.all():
        if symptoms.lower() in medicine.symptoms.lower():
            store = UserModel.objects.get(username=medicine.username)
            address=store.address
            if location.lower() in address.lower():
                medicine.store=store.name
                medicine.address=store.address
                medicines.append(medicine)
    return medicines

def getReviewsByMedicine(id):
    reviews = []
    for review in ReviewModel.objects.all():
        print(id,review.medicine)
        if id==review.medicine:
            print("in if")
            reviews.append(review)
    return reviews