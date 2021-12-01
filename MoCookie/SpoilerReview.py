from urllib.request import urlopen
from bs4 import BeautifulSoup

review_list = []
for page in range(1,5):
    url = f'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=198471&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page=3{page}'
    html = urlopen(url)
    soup = BeautifulSoup(html,'html.parser')
    for i in range(3):
        review = soup.find('span',{'id':f'_filtered_ment_{i}'})
        review = review.get_text().strip()
        review_list.append(review)

# with open을 활용하여 따로 file을 열고 닫기 하지 않아도 된다.
# 'w'는 file write 기능
# encoding='utf-8' => utf-8형식으로 저장
with open('MovieReview/SpeedReview.txt', 'w', encoding='utf-8') as f:
    for single_review in review_list:
        f.write('- '+single_review+'\n\n')

del review_list # 메모리 절약을 위한 리스트 삭제
