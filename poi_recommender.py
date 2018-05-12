import pandas as pd
import recommender_engine as re

def main():	
	df = pd.read_csv('data/cleaned_poi.csv')
	print('\n calculate tfidf')
	tfidf_matrix = re.get_tfidf(df.rev_cat_soup)
	print('matrix shape: ', tfidf_matrix.shape)
	cosine_sim = re.get_cosine_sim(tfidf_matrix)
	df_result = re.get_recommendation(df,'Tate Modern', 'place_name',cosine_sim)
	print(df_result[['place_name','relative_score','similarity_score','popularity_index','categories','reviews_combined']])
main()
