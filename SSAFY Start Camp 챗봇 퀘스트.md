# SSAFY Start Camp 챗봇 퀘스트

서울 1반 최현호,  https://github.io/popcon9424/chatbot/

## I. 스펙(Specification)

구현된 어플리케이션의 주요 기능

#### 1) 유명인 얼굴 인식 기능

- 사용자가 텔레그램을 통해 챗봇에게 전송한 데이터를 분석한다.

- 데이터가 photo일 경우, Clova Face Recognization(CFR)을 통해 얼굴 인식을 시작한다.
- 인식에 성공했을 경우, 해당 인물의 이름을 텍스트로 반환한다.

#### (2) 회신 기능

- 챗봇에 전송한 데이터가 photo가 아닌 text일 경우, 입력받은 텍스트만을 따로 저장한다.
- 저장된 데이터를 그대로 출력하여 회신한다.



## II. 회고(Retrospective)

#### (1) 유명인 얼굴 인식 기능

- 입력받은 데이터에서 정보를 저장할 때, 데이터 타입이 photo와 text 모두 아니라 file이었을 때, 텔레그램 서버에서 받아오는 것이 중단되지 않아서 요청이 계속 쌓이는 것 때문에 어려움이 있었다.
- 손댈 수 없는 부분이지만 인식의 정확성 자체가 너무 낮다는 문제점이 있다.



### III. 보완 계획(Feedback)

#### (1) 유명인 얼굴 인식 기능 보완

- 사진 예시를 몇 장 가지고 테스트했을 때, 일치했던 경우가 상당히 적어서 받아오는 데이터 중 정확도를 같이 반환할 예정이다.
- 데이터 타입은 photo 이지만, 풍경 또는 사물의 사진인 경우나 프로그램이 인식하지 못 할 만큼 얼굴이 작거나 흐릿할 때, 특정 문구를 반환하게끔 수정할 계획이다.

#### (2) 특정 키워드에 따른 반응

- 특정 키워드를 입력 시 키워드에 맞는 데이터를 웹 크롤링을 통해 수집하여 반환하는 기능을 추가할 예정이다. (예시 : 로또, 날씨, 실시간 검색어 등)

#### (3) photo, text 이외의 데이터 타입 입력 시

- 현재는 photo와 text 타입의 데이터만 결과값을 반환하지만, 텔레그램에서 보낼 수 있는 데이터에는 두 종류만 있는 것이 아니라 다른 타입의 데이터도 있다.
- 아직은 다른 타입의 데이터를 입력받으면 API에서 어떤 종류의 데이터를 주는 지는 모르지만 데이터 반환을 타입에 따라 다르게 할 계획이다.