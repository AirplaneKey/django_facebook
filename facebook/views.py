from django.shortcuts import render , redirect
from facebook.models import Article,Comment
# Create your views here.
cnt = 0
def play(request):
    return render(request, "play.html")

count =0
def play2(request):
    name = 'Lee JaeHa'
    global count
    diary = list()
    count = count + 1
    age = 25
    if age > 20:
        status = '성인입니다'
    else:
        status = '청소년입니다.'

    diary = ['날씨가 좋았다 - 월', '흐렸다 - 화','배고팠다 - 수']
    return render(request, "play2.html", {'name': name, 'cnt': count, 'status': status,
                                          'diary': diary})

def profile(request):
    return render(request, "profile.html")
def challenge(request):
    global cnt
    cnt = cnt + 1
    age = 25
    name = "이재하"
    if age >= 20:
        status = "(성인)입니다"
    else:
        status = "(청소년)입니다"
    if cnt == 7:
        result = "당첨!입니다."
    else:
        result = "꽝입니다."


    return render(request,
                  "challenge.html",
                  {'age': age, 'cnt': cnt,
                   'name': name, 'result': result, 'status': status})

def newsfeed(request):
    articles = Article.objects.all()
    return render(request, "newsfeed.html", {'articles': articles})

def detail_feed(request , pk):   # urls.py 에서 pk 때문
    article = Article.objects.get(pk=pk)
    #코멘트 추가 요청이 들어오면 DB에 등록하기
    if request.method == 'POST':
        #코멘트 등록하기
        Comment.objects.create(
            article= article,
            author= request.POST['nickname'],
            text = request.POST['reply'],
            password = "pw",
        )
    return render(request, "detail_feed.html", {'feed': article})

def neww_feed(request):
    temp = "-추신 : 감사합니다."
    #Django가 여기서 글을 등록해라
    # 1) 입력한 내용을 받아오기 1번
    if request.method == 'POST':
        #requset 는 받아오는
        feed = Article.objects.create(
            author=request.POST['author'],
            title=request.POST['title'],
            text=request.POST['content']+temp,
            password=request.POST['password'],
        )
       # return redirect(f'/feed/{feed.pk}')
        return redirect('/feed/'+str(feed.pk))
    # 2) 받은 글을 등록하기
    return render(request, 'neww_feed.html')

def edit_feed(request , pk):
    # 1) 수정한 글의 정보를 불러오기
    feed = Article.objects.get(pk=pk)

    if request.method == 'POST':
        feed.title = request.POST ['title']
        feed.author = request.POST['author']
        feed.text = request.POST['content']
        feed.save()

        #feed.pk  #글번호
        #return redirect(f'/feed/{feed.pk}/')높은 버전
        return redirect('/feed/' +str(feed.pk))
    return render(request,"edit_feed.html", {'feed': feed})

def remove_feed(request , pk):#pk를 널은 이유는 페이지의 번호를 알고싶을때
    feed = Article.objects.get(pk=pk)
    if request.method == 'POST':
        #삭제해주세요
        if request.POST['pw']==feed.password:
            feed.delete()
            return redirect("/")
        else:
            print("비밀번호가 틀렸습니다")
    return render(request,"remove_feed.html")

