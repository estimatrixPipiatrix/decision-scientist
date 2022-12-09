import pandas as pd
import re
# clean and save the amazon features and labels for
# both the training and test data

amazonTrain = pd.read_csv('train_no_commas.txt')
amazonTest  = pd.read_csv('test_no_commas.txt')
labelsTrain = pd.DataFrame(amazonTrain['review_text'].str[9])
labelsTest  = pd.DataFrame(amazonTest['review_text'].str[9])
labelsTrain = \
    labelsTrain.rename(columns={'review_text':'rating'})
labelsTest  = \
    labelsTest.rename(columns={'review_text': 'rating'})

# strip label text from amazon data frame
amazonTrain['review_text'] = \
        amazonTrain['review_text'].str[10:]
amazonTest['review_text'] = \
        amazonTest['review_text'].str[10:]

# make all lower case and remove punctuation
amazonTrain['review_text'] = \
    amazonTrain['review_text'].map(lambda x: \
    re.sub('[,\.!?:]','', x))
amazonTest['review_text'] = \
    amazonTest['review_text'].map(lambda x: \
    re.sub('[,\.!?:]','',x))
amazonTrain['review_text'] = \
    amazonTrain['review_text'].map(lambda x: x.lower())
amazonTest['review_text'] = \
    amazonTest['review_text'].map(lambda x: x.lower())

amazonTrain.to_pickle('train_clean.csv')
labelsTrain.to_pickle('train_labels_clean.csv')
amazonTest.to_pickle('test_clean.csv')
labelsTest.to_pickle('test_labels_clean.csv')
