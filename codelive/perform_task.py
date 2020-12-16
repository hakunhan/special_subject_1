class PerformTask:
    def __init__(self, list_books, list_users, dictionary_data):
        self.list_books = list_books
        self.list_user = list_users
        self.dictionary_data = dictionary_data

    # get average rating of each book then print to console
    def get_averages(self):
        averages = [0] * len(self.list_books)
        result = {}
        user_rating_list = []

        for i in range(0, len(self.dictionary_data)):
            user_rating_list.append(self.dictionary_data[self.list_user[i]])

        for i in range(0, len(averages)):
            rating_count = 0

            for j in range (0, len(user_rating_list)):
                if user_rating_list[j][i] == 0:
                    continue

                averages[i] += user_rating_list[j][i]
                rating_count+=1

            averages[i] = averages[i]/rating_count

        for i in range (0, len(averages)):
            result[self.list_books[i]] = averages[i]

        result = dict(sorted(result.items(), key=lambda item: item[1], reverse= True))

        for key in result:
            print("%s %.4f" % (key, result[key]))

        print("----------------------------------------")

    # get similarly of every user that the same with input user then print recommendation to console
    def get_recommendations(self):
        user = input("user? ")

        if user not in self.list_user:
            self.get_averages()

        similar_list = {}



