﻿아마존 구매대행 가격 비교 사이트 
===================


구매대행 사이트 별로 수수료가 다르기 때문에 가격이 상이합니다. 아마존 구매대행을 취급하는 사이트 가격정보를 모아서 비교해주는 사이트를 개발하는 프로젝트 입니다.

----------


개발 계획
-------------

```sequence
사이트->아마존 API: 물품 이름 
아마존 API-->사이트:ASIN목록 전송
사이트->크롤링 API: 사용자가 선택한 ASIN값을 전송
Note right of 크롤링 API: 각 사이트별 가격 정보 크롤링
크롤링 API-->사이트: 사이트에서 모은 가격 전송
```
크롤링 API는 python3로 개발중입니다.
사이트는 현재 개발이 필요합니다.


python3 API 개발 진행 상황
-------------

각 구매대행별로 가격을 어떻게 크롤링할지 연구 중입니다.

3가지 유형으로 가격을 크롤링합니다.

1. 가격이 HTML코드에 적혀서 response되는 경우
 - beautifulsoup를 이용하여 tag를 따라 크롤링합니다.
2. javascript코드로 가격을 다시 서버에 요청하는 경우
 - XHRrequest를 통해 서버에 가격정보를 요청하여 받아옵니다.
3. 자체 javascript로 가격을 계산하는 경우
 - 같은 로직을 작성하여 가격을 계산합니다.

현재까지 연구한 구매대행

1. 보다존  : tag => script 계산

2. 바이잇나우 :  XHRrequest 요청

3. 몰베이 : tag=> XHRrequest  요청 =>tag

4. 아마존365 :  tag=> script 계산

5. 조이베이 : 아직 진행중

6. 유스엔조이 : response가 될때도 있고 안될때도

7. 바이비 :  tag=> javascript parser가 필요






ASIN 값 : B079P5D9BC 을 예제로 구현된 코드는 parsing_logic.py로 업로드 되어있습니다.

앞으로 모든 구매대행의 가격정보를 모으는 코드를 작성후 각각 멀티쓰레드로 구현할 예정입니다.


사이트 개발 진행 상황
-------------

1. front server와 backend server를 분리하여 개발 환경을 구축할 예정입니다.

java와 tomcat을 사용하여 개발중입니다. 조만간 예제 코드가 올라 갈 예정입니다.


구현할 기능

1. 사용자에게 물품명을 input으로 받는다.
2. 아마존 API에게 ASIN값 목록을 받아온다.
3. ASIN목록과 상세 내용을 사용자에게 보여준다.
4. 사용자가 ASIN을 고르면 가격정보를 API에게 요청한다.
5. 가격정보를 사용자에게 보여준다.
