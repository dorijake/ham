
각 어플리케이션 내부 static/tempates 필요시 아래 경로로 생성
static : (appname)/static/(appname)/(css, js, images)/
templates : (appname)/templates/(appname)/~.html
*
*
*
*

각 app 내에서 공통적으로 사용되는 템플릿은 (appname)/templates/(appname)/base.html 로 생성한 뒤 {% extends 'base.html' %} 로 프로젝트 폴더(ham) 내 base.html을 확장할 것
app 공통 템플릿 내부 컨텐츠 블록 :  {% block (appname) %}

필요한 스크립트는 block의 가장 밑에 script 태그 작성
*
*
*
*

Applications 개요

user : User 관련 model 및 회원 가입, 개인 정보 수정 템플릿

net : 네트워크 서비스 출력 관련 템플릿 

home : 홈 화면 템플릿 위주

service : 추후 음식점 혜택 서비스 기능

neo : graph DB 관련

shop : 상점 관련 Model 및 상점  등록/ 관리 템플릿

