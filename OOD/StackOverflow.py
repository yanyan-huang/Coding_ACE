"""
Design StackOverflow 

1. functional requirement
-users post questions and answers
-comments, votes, tags, reputation for author(votes)
-support search, notification
- real-time collaboration

2. core use cases:
Post
- post a question
- post a answer 
-delete post, edit post
Interaction:
- upvote/downvote
- comment on post 
Search:
-search/filter question 


3. entity:
User - id, email, name, reputation(votes)
Question - queston_id, title, body, tags:list, authorid(User),timestamp,votes
Answer -answer_id, questionid, body, authorid(User),timestamp,votes
Comment(Question/ Answer) - id, body, parentid(Question/Answer),authorid
tag: id, name, questionid 
Reputation : id, userid(Optional)
vote: id, targetid(Question/Answer), type(upvote/downvote)

4. relationships
one User can post many questions, answers, comments
one question can have many answers, comments
oen answer belongs to one question 
one comment belongs to one question or one answer 
one vote target to one question or answer 
one tag could associate with many questions 

5. Design 


"""
from datetime import datetime 
class User:
    def __init__(self, userid:int, name: str):
        self.userid = userid 
        self.name = name 
        self.reputaiton = 0
        self.questions=[] 
        self.answers =[]
    def post_question(self, title, body, tags):
        q = Question(len(self.questions)+1, body, self, title, tags)
        self.questions.append(q)
        return q 

        
    def post_answer(self, body, question):
        a = Answer(len(self.answers)+1, body, self, question)
        self.answers.append(a)
        return a
        
    def vote(self, post, upvote):
        post.vote(upvote)
        self.reputation += 1 if upvote else -1 

        
class Post: # Question and Answer 
    def __init__(self, post_id:int, body: str,author:User):
        self.post_id = post_id
        self.body = body 
        self.author = author
        self.timestamp = datetime.now()
        self.vote = 0
        self.comments = [] # comment list for answers or questions 
    def vote(self,upvote):
        self.votes += 1 if upvote else -1
    def add_comment(self, comment):
        self.comments.append(comment)
        
class Question(Post):
    def __init__(self, post_id: int, body:str, author:User, title: str, tags:list ):
        super().__init__(post_id, body, author)
        self.title  = title 
        self.tags = tags
        self.answers =[]

class Answer(Post):
    def __init__(self, post_id: int, body, author, question:Question):
        super().__init__(post_id, body, author)
        self.question = question
class Comment:
    def __init__(self, comment_id:int, author:User, body:str):
        self.comment_id = comment_id
        self.author = author
        self.body = body 
        self.timestamp = datetime.now()


alice = User(1, "Alice")
bob = User(2, "Bob")
q1 = alice.post_question("How to learn OOD","How should i prepare for Amazon OOD question?","Code")
a1 = bob.post_answer(" GO to Awesome repo.",q1)
print(f"Question:{q1.title}")
print(f"Answer:{a1.body}")

