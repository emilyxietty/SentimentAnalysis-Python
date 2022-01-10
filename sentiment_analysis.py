# Create universal variables for latitude, longitude and tweets list
latitude_list = []
longitude_list = []
tweet_words_list = []


# Function to create keyword dictionary
def create_keyword_dict(filename):
    # Try and except statement
    try:
        score_dict = {}
        # Opening file with keywords
        keywords_file = open(filename, "r", encoding="utf8")

        for keywords_line in keywords_file:
            # Separating words and values in line
            key_sect = keywords_line.strip().split(",")
            # Equating value and word in dictionary
            score_dict[str(key_sect[0])] = int(key_sect[1])
        return score_dict

    except IOError:
        print("File not found")
        quit()


# Function to organize list of tweets
def create_tweet_list(filename):
    # Try and except statement
    try:
        final_list = []
        # Opening file with keywords
        tweet_file = open(filename, "r", encoding="utf8")

        for tweet_line in tweet_file:
            # Separating tweets by whitespace
            tweet_sect = tweet_line.split(" ")

            # assigning variables and cleaning tweets
            lat = tweet_sect[0].strip("[,")
            lat = float(lat)

            long = tweet_sect[1].strip("]")
            long = float(long)

            latitude_list.append(lat)
            longitude_list.append(long)

            tweet_words = tweet_sect[5:]
            tweet_words = str(tweet_words).lower().strip("!.?,")
            tweet_words_list.append(tweet_words)
        return tweet_words_list

    except IOError:
        print("File not found")
        quit()


# Function to compute tweets
def computes_tweets(keyword_file, tweet_file):
    # Creating keyword dictionary
    keyword_dict = create_keyword_dict(keyword_file)
    # Creating organized list of tweets
    tweet_list = create_tweet_list(tweet_file)

    # Initializing happiness values
    east_hap = 0
    cent_hap = 0
    mount_hap = 0
    pac_hap = 0

    # Creating count variables for different regions
    pac_count = 0
    mount_count = 0
    cent_count = 0
    east_count = 0

    # Creating sum variables for different regions
    pac_sum = 0
    mount_sum = 0
    cent_sum = 0
    east_sum = 0

    # Creating count for loop
    count = 0
    for tweet_line in tweet_list:
        for element in keyword_dict:
            if element in tweet_line:
                # Ridding tweets outside of the latitude
                if 24.660845 < latitude_list[count] < 49.189787:
                    # Tweets in the pacific region
                    if -125.242264 < longitude_list[count] < -115.236428:
                        pac_count += 1
                        pac_sum += keyword_dict[element]
                        pac_avg = pac_sum / pac_count
                        pac_hap = (pac_avg, pac_count) # Creating tuple with average and sum

                    # Tweets in the mountain region
                    elif -115.236428 < longitude_list[count] < -101.998892:
                        mount_count += 1
                        mount_sum += keyword_dict[element]
                        mount_avg = mount_sum / mount_count
                        mount_hap = (mount_avg, mount_count) # Creating tuple with average and sum

                    # Tweets in the central region
                    elif -101.998892 < longitude_list[count] < -87.518395:
                        cent_count += 1
                        cent_sum += keyword_dict[element]
                        cent_avg = cent_sum / cent_count
                        cent_hap = (cent_avg, cent_sum) # Creating tuple with average and sum

                    # Tweets in the eastern region
                    elif -87.518395 < longitude_list[count] < -67.444574:
                        east_count += 1
                        east_sum += keyword_dict[element]
                        east_avg = east_sum / east_count
                        east_hap = (east_avg, east_sum) # Creating tuple with average and sum
        count += 1

    # Creating final list from regional lists
    hap_list = [east_hap, cent_hap, mount_hap, pac_hap]

    # Presentation of results
    print("The Eastern happiness average and number of tweets respectively are", hap_list[0])
    print("The Central happiness average and number of tweets respectively are", hap_list[1])
    print("The Mountain happiness average and number of tweets respectively are", hap_list[2])
    print("The Pacific happiness average and number of tweets respectively are", hap_list[3])
