from pymongo import MongoClient

class Pymongodb:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client.local  # 'local' 데이터베이스 사용

    def insert_data(self):
        # 책 데이터 삽입
        books = [
            {"title": "Kafka on the Shore", "author": "Haruki Murakami", "year": 2002},
            {"title": "Norwegian Wood", "author": "Haruki Murakami", "year": 1987},
            {"title": "1Q84", "author": "Haruki Murakami", "year": 2009}
        ]
        self.db.books.insert_many(books)

        # 영화 데이터 삽입
        movies = [
            {"title": "Inception", "director": "Christopher Nolan", "year": 2010, "rating": 8.8},
            {"title": "Interstellar", "director": "Christopher Nolan", "year": 2014, "rating": 8.6},
            {"title": "The Dark Knight", "director": "Christopher Nolan", "year": 2008, "rating": 9.0}
        ]
        self.db.movies.insert_many(movies)

        # 사용자 행동 데이터 삽입
        user_actions = [
            {"user_id": 1, "action": "click", "timestamp": "2023-04-12T08:00:00Z"},
            {"user_id": 1, "action": "view", "timestamp": "2023-04-12T09:00:00Z"},
            {"user_id": 2, "action": "purchase", "timestamp": "2023-04-12T10:00:00Z"}
        ]
        self.db.user_actions.insert_many(user_actions)

        print("Data inserted successfully")
        self.print_line()

    # 1. 특정 장르의 책 찾기
    def find_books_by_genre(self, genre):
        print("--- Find books by genre ---")
        query = {"genre": genre}
        project = {"_id": 0, "title": 1, "author": 1}
        books = self.db.books.find(query, project)

        for book in books:
            print(book)
        self.print_line()

    # 2. 감독별 평균 영화 평점 게산
    def calc_avg_movie_score(self):
        print("--- Calc Avg Movie Score ---")
        query = [
            { "$group": { "_id": "$director", "avg_score": { "$avg": "$rating" }}},
            { "$sort": { "avg_score": -1 } }
        ]
        calc_result = self.db.movies.aggregate(query)
        
        for result in calc_result:
            print(result)
        self.print_line()

    # 3. 특정 사용자의 최근 행동 조회
    def user_recently_action(self, user_id):
        print("--- User Recently Action ---")
        
        query = [
            { "$match": { "user_id": user_id } },
            { "$sort": { "timestamp": -1 } },
            { "$limit": 1 },
            { "$project": { "_id": 0 } }
        ]

        search_result = self.db.user_actions.aggregate(query)
        print(list(search_result))
        self.print_line()

    # 4. 출판 연도별 책의 수 계산
    def count_books_by_year(self):
        print("--- Count Books By Year ---")
        
        query = [
            { "$group": { "_id": "$year", "quantity": { "$sum": 1 } } },
            { "$sort": { "quantity": -1 } }
        ]
        count_result = self.db.books.aggregate(query)
        
        for result in count_result:
            print(result)
        self.print_line()

    # 5. 특정 사용자의 행동 업데이트
    def update_user_actions(self, user_id, timestamp):
        print("--- Update User Actions ---")

        query = { "user_id": user_id, "action": "view" ,"timestamp": { "$lt": timestamp } }
        update = { "$set": { "action": "seen" } }
        self.db.user_actions.update_many(query, update)
        self.print_line()
    
    # 사용자의 행동 확인
    def print_user_actions(self):
        print("--- Print User Actions ---")
        actions = self.db.user_actions.find({}, { "_id": 0 })
        
        for action in actions:
            print(action)
        self.print_line()

    # 데이터베이스 닫기
    def close_db(self):
        self.client.close()
        print("Connection Closed.")
        self.print_line()

    # 텍스트 라인 출력
    def print_line(self):
        print("-" * 50)

if __name__ == "__main__":
    pymongodb = Pymongodb()
    
    pymongodb.insert_data()
    # 1. fantasy 장르의 책 검색
    pymongodb.find_books_by_genre("fantasy")
    # 2. 감독별 영화 평점 평균 조회
    pymongodb.calc_avg_movie_score()
    # 3. 1번 사용자의 최근 행동 조회
    pymongodb.user_recently_action(1)
    # 4. 출판 연도별 책의 수 계산
    pymongodb.count_books_by_year()
    # 5. 특정 사용자의 행동 업데이트
    pymongodb.update_user_actions(1, "2023-04-10")
    pymongodb.print_user_actions()
    
    pymongodb.close_db()