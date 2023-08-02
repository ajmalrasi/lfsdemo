import pandas as pd


class TvShow:

    def __init__(self, year) -> None:
        """
            _summary_

        Args:
            year int: Year
        """

        self.year = year
        self.df = pd.read_csv('tv_shows.csv')
        self.data = self.df[self.df["Year"] == self.year]

    def show_count(self):
        """
            Number of TV shows released 

        Returns:
            int: count
        """
        print("Number of TV shows released {}".format(len(self.data)))
        return len(self.data)


    def best_series(self):
        """
            Best Series Based on IMDb, 
            Best Series Based on Rotten Tomatoes 
        """
        max_rt_idx = self.data["Rotten Tomatoes"] \
                        .str.extract('(\d+)') \
                        .fillna(0) \
                        .astype(int) \
                        .idxmax()

        max_imdb_idx = self.data.IMDb.idxmax()

        print("Best IMDB TV Show : {}, Best Rotten Tomatoes TV Show : {}"
               .format(self.data["Title"][max_imdb_idx]
               ,self.data["Title"][max_rt_idx]) )

    def best_rated_show(self):
        """
            Best rated show out of Rotten Tomatoes
            and IMDB

        Returns:
            int: index of best rating
        """
        best_idx = self.average_rating().idxmax()

        print("Best TV Show {}" \
                .format(self.data["Title"][best_idx]) )

        return best_idx



    def best_series_adult(self):
        """
            Best 18+ TV Show
            and 18- TV Show
        """
        rt_df = self.data["Rotten Tomatoes"] \
                        .where(self.data["Age"] == "18+") \
                        .str.extract('(\d+)') \
                        .fillna(0) \
                        .astype(float) / 10

        eightheen_idx = (rt_df.add(self.data.IMDb
                        .where(self.data["Age"] == "18+"), 
                    axis=0) / 2).idxmax()

        non_rt_df = self.data["Rotten Tomatoes"] \
                .where((self.data["Age"] != "18+") 
                     & (self.data["Age"] != "all")) \
                .str.extract('(\d+)') \
                .fillna(0) \
                .astype(float) / 10                 
        
        non_eighteen_idx = (non_rt_df.add(self.data.IMDb.where(
                                (self.data["Age"] != "18+") & 
                                (self.data["Age"] != "all") ), 
                        axis=0) / 2).idxmax()

        print("Best 18+ TV Show {}, Best 18- TV Show {}"
               .format(self.data["Title"][eightheen_idx]
               ,self.data["Title"][non_eighteen_idx]) )

    
    def average_rating(self):
        """
        Average Rating out of 10

        Returns:
            dataframe: Average rating
        """

        rt_df = self.data["Rotten Tomatoes"] \
                        .str.extract('(\d+)') \
                        .astype(float) / 10

        rt_df = rt_df.fillna(rt_df.mean())

        return (rt_df.add(self.data.IMDb.
                    fillna(self.data.IMDb.mean()), axis=0) / 2)

