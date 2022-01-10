import sentiment_analysis


# Main Function
def main():

    # Input for files for function
    keyword_file = input("Please insert the keyword file: ")
    tweet_file = input("Please insert the tweets file: ")

    #Calling function to compute tweets with the inputted files
    sentiment_analysis.computes_tweets(keyword_file, tweet_file)


main()
