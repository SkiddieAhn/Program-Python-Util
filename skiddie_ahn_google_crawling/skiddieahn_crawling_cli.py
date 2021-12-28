from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import urllib.request

'''
크롤링: selenium
이미지 다운로드: urllib.request
경로 관련: os
시간 관련: time
참고 자료: https://yobbicorgi.tistory.com/29?category=478264
'''
# =============================================================================
# <함수> 파일 생성 
# =============================================================================
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. '+ directory)
        
# =============================================================================
# <함수> 파일명 정렬
# =============================================================================

def sortAndRename(directory,keyword):
    file_list = [f for f in os.listdir(directory) if '.jpg' in f]
    num_list = sorted([int(l.split('_')[1].split('.')[0]) for l in file_list])
    for idx in range(len(file_list)):
          src_file = directory +'/'+ keyword +'_{}.jpg'.format(num_list[idx])
          output = directory + '/'+ keyword +'_{}.jpg'.format(idx)
          print('{} --> {}'.format(src_file, output))
          os.rename(src_file, output)
          
# =============================================================================
# 드라이버 및 경로 설정 + 검색 키워드 설정
# =============================================================================
print('드라이버 및 경로 설정 .....')
keyword='fruit apple' # <================== keyword 수정해서 사용하면 됨
createFolder('./'+keyword+'_img_download')

chromedriver ='./chromedriver.exe'
driver=webdriver.Chrome(chromedriver)
driver.implicitly_wait(3)

# =============================================================================
# 구글 이미지 검색 접속 및 키워드 입력
# =============================================================================
print(keyword,'검색 .....')
driver.get('https://www.google.co.kr/imghp?hl=ko')

Keyword=driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')
Keyword.send_keys(keyword)

driver.find_element_by_xpath('//*[@id="sbtc"]/button').click()

# =============================================================================
# 스크롤링
# =============================================================================
print(keyword,'스크롤 중 .....')
elem=driver.find_element_by_tag_name('body')
for i in range(60):
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.1)

try:
    driver.find_element_by_class_name('mye4qd').click() # '결과 더 보기' 클릭
    for i in range(60):
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.1)
except:
    print(keyword+' 스크롤 실패')
    pass

# =============================================================================
# 이미지 개수 세기
# =============================================================================
print(keyword,'다운로드 준비 중 .....')
links=[]
images=driver.find_elements_by_css_selector('img.rg_i.Q4LuWd') # 페이지 요소 다중 선택 (클래스명 기준)
for image in images:
    if image.get_attribute('src')!=None:
        links.append(image.get_attribute('src'))

print(keyword,'찾은 이미지 개수:',len(links))
time.sleep(2)

# =============================================================================
# 이미지 다운로드
# =============================================================================
for k,i in enumerate(links):
    url=i
    start=time.time()
    try:
        urllib.request.urlretrieve(url,'./'+keyword+'_img_download/'+keyword+'_'+str(k)+'.jpg')
        print(str(k+1)+'/'+str(len(links))+' '+keyword+' 다운로드 중...... Download time : '+str(time.time()-start)[:5]+'초')
    except:
        print(str(k+1)+'/'+str(len(links))+' '+keyword+' 다운로드 실패......')
        pass
    if k+1 == len(links):
        print(keyword,'이미지 크롤링 완료')

driver.close()

