# Project : WordNote  
  
**Hanyang Univ. ERICA Open Source Software Project**   

## Who?
소프트웨어학부 2019052851 박준성  ( hell-o-world@naver.com )

---
## What?  
영단어장을 CLI로 구현한 프로그램.  
쉽게 말하자면, 명령어로 영단어장을 관리하는 프로그램이다.

---
## Why?  
오프라인에서도 사용할 수 있는 나만의 단어장을 만들고 싶었다.

---
## NOTICE  
**해당 프로그램은 1440*900 해상도 우분투 터미널 최대화 화면에 최적화되어 있습니다.**   
**또한 임의로 data 디렉토리 내의 파일을 수정하면 예기치 못한 에러가 발생할 수 있습니다.**  

---
## How to Build 

### Ubnutu 18.04
1. 우분투 터미널에  `sudo apt install python3` 을 입력하여 python3을 설치한다.
2. 현재 이 페이지 상단에 있는 초록색 `Clone or download` 버튼을 누른 후 `Download Zip` 을 클릭한다.
3. 원하는 위치에 압축을 해제한다.
4. 우분투 터미널에서 압축을 해제한 폴더가 있는 디렉토리로 이동한다.
5. 우분투 터미널에 `cd ERICA_WordNote-master/wordnote` 를 입력한다.
6. 우분투 터미널에 `python3 main.py` 를 입력하여 프로그램을 실행한다.
  
### Windows 10
1. [이 곳](https://www.python.org/downloads/)에 들어간다.  
2. 상단 화면 좌측에 있는 노란색 `Download Python 3.8.1` 버튼을 누른 후 설치를 진행한다.  
3. 현재 이 페이지 상단에 있는 초록색 `Clone or download` 버튼을 누른 후 `Download Zip` 을 클릭한다.
4. 원하는 위치에 압축을 해제한다.  
5. 압축을 해제한 폴더로 들어가, wordnote 폴더를 들어간다.  
6. main.py를 더블클릭하여 프로그램을 실행한다.    

---
## How to Simulate 
사용자가 추가한 단어들은 'STAR'라고 불리는 특별한 단어장에 모두 기록됩니다.  
사용자가 만든 단어장에서 단어를 추가한다면, STAR에서 기록된 그 단어의 인덱스값을 추가하여 참조하게 합니다.  
따라서 STAR의 내용을 직접적으로 수정하는 명령어는 해당 내용을 참조하는 모든 단어장에 영향을 미칩니다. 

또한 이 프로그램에는 '접속'이라는 개념이 있습니다.  
접속은 사용자가 만든 단어장 하나를 주 작업영역으로 삼는 것입니다.  
STAR에 단어를 추가할 때, 접속중인 단어장에도 해당 단어를 추가합니다.  
그 밖에도, STAR에 이미 존재하는 단어를 끌어다 사용하거나, 단어장이 참조 중인 단어들을 확인할 수 있습니다.

---
## How to Command

명령어는 명령 부분, 인수 부분, 옵션 부분으로 나누어져 있습니다.  
명령어 구성 순서는 명령부, 인수부, 옵션부로 이루어져야 하며,  
각 부분들 사이는 하나의 공백으로 구분합니다. (이를 어기면 명령어가 수행되지 않을 수 있습니다.)   
인수부 또는 옵션부를 필수로 작성하지 않아도 되는 경우도 있고, 필수로 작성해야 하는 부분도 있습니다.  

옵션부는 옵션 명령부와 옵션 인수부로 나누어집니다.  
복수 개의 인수를 받는 경우, 콤마(,)로 구분하여 입력을 받아야 합니다.  

명령부를 약어로 쓸 수 있는 경우, (명령부) : (명령부의 약어) 로 표기합니다.  

### Note
1. **addnote : an**  
`addnote (등록하고자 하는 단어장 이름)`  
**단어장을 추가하는 명령어입니다.**  
단어장 이름의 정규표현식은 다음과 같습니다 : `[a-zA-Z ㄱ-ㅎ가-힣()ㅏ-ㅣ0-9_.-]*`  
단어장 이름의 양 끝에 공백이 올 수 없으며, 이름의 길이가 100자가 넘지 않아야 합니다.  
같은 이름의 단어장이 존재한다면, 지우고 새로운 단어장을 만들 것인지 묻습니다.  
  
2. **removenote : rn**    
`removenote (삭제하고자 하는 단어장 이름)`  
**단어장을 삭제하는 명령어입니다.**  
해당 이름의 단어장이 존재한다면, 정말 지울 것인지 한번 더 묻고 그렇다고 하면 지웁니다.  
  
3. **connectnote : cn**   
`connectnote (접속하고자 하는 단어장 이름)`  
**단어장에 접속하는 명령어입니다.**    
접속중인 단어장이 있으면 사용할 수 없습니다.  
  
4. **disconnectnote : dn**  
`disconnectnote`  
**접속중인 단어장으로부터 벗어나는 명령어입니다.**  
해당 명령어는 어떤 인수도 갖지 않습니다.  

5. **mergenote : mn**  
`mergenote (합병하고자 하는 단어장들)`  
**여러 개의 단어장들을 합쳐서 하나의 단어장을 만드는 명령어입니다.**  
합병하고자 하는 단어장의 갯수가 실질적으로 1개 이상이어야 합니다.  
알 수 없는 단어장이 없다면 합병될 단어장의 이름을 입력받습니다.  
이는 `-name (합병될 단어장의 이름)` 옵션을 사용해 미리 정할 수 있습니다.     
접속중인 단어장이 있으면 사용할 수 없습니다.   
  
6. **viewnote : vn**  
`viewnote`  
**단어장이 참조하고 있는 단어들을 보여주는 명령어입니다.**  
`-print` 옵션을 추가하여 data/view/ 디렉토리에 txt 파일로 출력할 수 있습니다.  
아무런 입력없이 엔터를 눌러 다음화면으로, b를 입력하여 이전화면으로,  
보고자 하는 페이지 번호를 입력하여 그 화면으로, q를 눌러 바로 종료할 수 있습니다.  
접속중인 단어장이 없으면 사용할 수 없습니다.  
  
### Word  
1. **newword : nw**  
`newword (등록하고자 하는 영단어)`  
**STAR에 없는 영단어를 등록하는 명령어입니다.**   
영단어의 정규 표현식은 다음과 같습니다 : `[a-zA-Z -]*`  
최소 하나의 의미 옵션을 포함해야 합니다.  
다음 옵션들은 의미 옵션입니다 : `-n` `-v` `-a` `-ad` `-prep` `-conj` `-pron` `-int`  
의미 옵션의 인수는 단수 또는 복수 개의 의미들로 가져야 합니다.  
의미의 정규 표현식은 다음과 같습니다 : `[ㄱ-ㅎ가-힣()ㅏ-ㅣ 0-9]*`  
의미 옵션의 인수는 세미콜론(;)으로도 구분할 수 있으며, 이 경우 뜻이 특별히 구분됩니다.  
한 영단어가 갖는 의미들은 서로 중복되지 않아야 합니다.  
접속중인 단어장이 있다면, 추가한 단어를 참조하게 합니다.
  
2. **appendword : aw**  
`appendword (새로운 뜻을 등록하고자 하는 영단어 or 그것의 STAR 인덱스 번호)`  
**STAR에 이미 있는 영단어에 새로운 뜻을 등록하는 명령어입니다.**   
newword 명령어의 문법과 동일합니다.  
접속중인 단어장이 있다면, 추가한 단어를 참조하게 합니다.  
  
3. **viewword : vw**  
`viewword (뜻을 보고자 하는 영단어)`  
**단어장이 참조하고 있는 단어의 뜻을 화면에 출력하는 명령어입니다.**  
`-star` 옵션을 통해 STAR에 저장된 해당 단어의 모든 뜻을 출력할 수 있습니다.  
이 옵션을 사용하지 않으면서 접속중인 단어장이 없다면 사용할 수 없습니다.  
  
4. **pullword : pw**  
`pullword (단어장이 참조하게끔 하고자 하는 영단어)`  
**STAR에 있는 단어를 사용자가 만든 단어장에 참조할 수 있도록 하는 명령어입니다.**  
`-all` 옵션을 통해 그 단어의 모든 뜻을 모두 가져올 수 있고,  
`-opt (가져오고자 하는 뜻 번호들)` 옵션을 통해 일부만 가져올 수도 있습니다.  
하지만 두 개의 옵션을 동시에 쓸 수는 없고, 어떤 옵션도 쓰지 않았을 경우,  
해당 단어의 모든 뜻들을 보여준 후, 가져오고자 하는 단어의 뜻 번호를 입력받는다.  
접속중인 단어장이 없다면 사용할 수 없습니다.  
  
5. **eraseword : ew**  
`eraseword (단어장이 참조하지 않게끔 하고자 하는 영단어)`  
**사용자가 만든 단어장이 참조하고 있는 단어의 뜻을 지우는 명령어입니다.**  
pullword 명령어의 문법과 동일합니다.  
접속중인 단어장이 없다면 사용할 수 없습니다.  
  
6. **deleteword : dw**  
`deleteword (지우고자 하는 뜻이 있는 영단어)`  
**STAR에 등록된 단어의 뜻을 지우는 명령어입니다.**  
pullword 명령어의 문법과 동일합니다.  
해당 단어의 뜻을 참조하고 있는 단어장의 목록을 보여주고 삭제할 것인지 묻습니다.  
삭제를 원한다면, STAR와 해당 단어장들에서 그 뜻을 제거합니다.  
접속중인 단어장이 있다면 사용할 수 없습니다.  

7. **modifyword : mw**  
`modifyword (수정하고자 하는 뜻이 있는 영단어)`  
**STAR에 등록된 단어의 뜻을 수정하는 명령어입니다.**  
해당 단어의 뜻을 모두 보여주고, 수정하고자 하는 뜻 번호를 입력받습니다.  
`-opt (수정하고자 하는 뜻 번호)` 옵션을 통해 위 과정을 생략할 수 있습니다.  
그 후, 단어의 뜻을 어떻게 수정할 지 입력을 받습니다.  
문장 맨 앞에 +를 붙인다면 단어의 뜻을 추가하고, -를 붙인다면 해당 뜻을 제거합니다.  
그 외의 경우에는 사용자에게 받은 입력 그대로 수정됩니다.    
접속중인 단어장이 있다면 사용할 수 없습니다.   

8. **checkword : cw**    
`checkword (존재여부를 확인하고자 하는 영단어)`   
**STAR에 등록된 단어인지 여부와 어떤 단어장이 참조하고 있는지 확인하는 명령어입니다.**  
접속중인 단어장이 있다면 사용할 수 없습니다.  
   
### ETC  
1. **exit**   
`exit`  
**프로그램을 종료하는 명령어입니다.**
  
2. **break**  
`break`  
**단어장의 접속을 강제로 끊어 변경사항을 저장하지 않는 명령어입니다.**   
  
3. **notelist : nl**  
`notelist`  
**만들어진 단어장들의 목록을 보여주는 명령어입니다.**

---
## Bug Fixed  
   
1. 단어장의 이름이 100자를 넘어도 단어장이 생성되던 버그를 고침  
2. viewnote 명령어가 접근한 단어장이 없을 때 사용하면 강제 종료되는 버그를 고침  
3. 이미 존재하는 단어장의 이름을 addnote 명령어로 추가시, 추가하지 않겠다고 해도 비정상적으로 추가되는 버그를 고침  
4. mergenote 명령어의 name 옵션이 정상적으로 적용되지 않은 버그를 고침  
5. viewnote 명령어에 print 옵션을 적용하면 강제 종료되는 버그를 고침  
6. appendword 명령어가 인덱스값으로 인수를 받지 못하던 버그를 고침   
7. 삭제하지 않은 디버그용 print문을 삭제함  
8. mergenote 명령어로 이미 존재하는 단어장의 이름을 사용할 수 있는 버그를 고침  
9. appendword 명령어에서 접속중인 단어장이 없어도 단어장의 이름을 출력하는 버그를 고침  
10. pullword 명령어에서 오타 수정  
    
---
  
**오류를 발견하셨다면 hell-o-world@naver.com 으로 data/log.txt 을 보내주시면 감사하겠습니다!!**