요즈음은 구글 번역이 상당한 수준으로 올라서 번거로운 번역작업의 초안 용도로 손색이 없다. 나도 여러가지 이유로 번역을 하게 되는데, 그러한 번역 작업에도 자주 이용하고 있다. 모르는 단어만 찾아보거나 어려운 문장만 복붙(복사-붙여넣기)해도 되지만, 코딩으로 한꺼번에 번역해주면 시간을 절약할 수 있지 않을까?

```python
import io
with io.open('input.txt', 'rt', newline='\n') as f:
    lines = [line.rstrip() for line in f]
print(len(lines), 'lines imported.')
```

    270 lines imported.

워드로 저장된 번역할 내용을 txt 형태로 저장했다. 저장할 때 CR, LF 를 묻게 되는데, 줄바꿈을 하는 방법을 설정하는 것이다. Carriage Return 이든 Line Feed 이든지 굳이 이해할 필요는 없는데, CR은 ‘\\r' , LF는 ‘\\n' 이라는 문자가 줄 뒤에 붙어서 저장되므로 이걸 어떤 형식 저장하는가에 따라서 불러올 때 이를 다르게 적용시켜야 한다.

1) 나는 LF 로 저장했으므로 open 의 parameter 에 newline=’\\n’ 을 추가하였다. ‘\\n' 을 만나면 새로운 줄로 인식해라 라는 뜻이다.

2) 하지만 문장마다 뒤에 이렇게 글자가 추가되는 것은 곤란하다.\\n

그래서 .rstrip() 으로 뒤에 붙는 chomp를 다 지워버리자.

---

혹시 추가로 알고 싶은 사람을 위해 위키 ([https://ko.wikipedia.org/wiki/새줄\_문자](https://ko.wikipedia.org/wiki/%EC%83%88%EC%A4%84_%EB%AC%B8%EC%9E%90)) 에서 설명하는 내용을 추가한다

***새줄 문자**(newline)는 [텍스트](https://ko.wikipedia.org/wiki/%ED%85%8D%EC%8A%A4%ED%8A%B8 "텍스트")의 한 줄이 끝남을 표시하는 [문자](https://ko.wikipedia.org/wiki/%EB%AC%B8%EC%9E%90 "문자") 또는 [문자열](https://ko.wikipedia.org/wiki/%EB%AC%B8%EC%9E%90%EC%97%B4 "문자열")이다. **개행 문자**, **줄바꿈 문자**(line break), **EOL**(end-of-line)과 같은 뜻이다. 기종이나 [운영 체제](https://ko.wikipedia.org/wiki/%EC%9A%B4%EC%98%81_%EC%B2%B4%EC%A0%9C "운영 체제")에 따라 새줄 문자를 나타내는 코드가 다를 수도 있다. 그래서 텍스트를 다른 시스템으로 전송할 때 새줄 문자의 치환 작업도 필요하다.*

LF[멀틱스](https://ko.wikipedia.org/wiki/%EB%A9%80%ED%8B%B1%EC%8A%A4 "멀틱스"), [유닉스](https://ko.wikipedia.org/wiki/%EC%9C%A0%EB%8B%89%EC%8A%A4 "유닉스"), [리눅스](https://ko.wikipedia.org/wiki/%EB%A6%AC%EB%88%85%EC%8A%A4 "리눅스"), [제닉스](https://ko.wikipedia.org/wiki/%EC%A0%9C%EB%8B%89%EC%8A%A4 "제닉스"), [AIX](https://ko.wikipedia.org/wiki/AIX "AIX"), [OS X](https://ko.wikipedia.org/wiki/OS_X "OS X"), [FreeBSD](https://ko.wikipedia.org/wiki/FreeBSD "FreeBSD")CR+LF[DEC TOPS-10](https://ko.wikipedia.org/w/index.php?title=DEC_TOPS-10&action=edit&redlink=1 "DEC TOPS-10 (없는 문서)"), [RT-11](https://ko.wikipedia.org/w/index.php?title=RT-11&action=edit&redlink=1 "RT-11 (없는 문서)"), [CP/M](https://ko.wikipedia.org/wiki/CP/M "CP/M"), [MP/M](https://ko.wikipedia.org/w/index.php?title=MP/M&action=edit&redlink=1 "MP/M (없는 문서)"), [도스](https://ko.wikipedia.org/wiki/%EB%8F%84%EC%8A%A4 "도스"), [OS/2](https://ko.wikipedia.org/wiki/OS/2 "OS/2"), [윈도](https://ko.wikipedia.org/wiki/%EB%A7%88%EC%9D%B4%ED%81%AC%EB%A1%9C%EC%86%8C%ED%94%84%ED%8A%B8_%EC%9C%88%EB%8F%84 "마이크로소프트 윈도"), [심비안 OS](https://ko.wikipedia.org/wiki/%EC%8B%AC%EB%B9%84%EC%95%88_OS "심비안 OS"), [팜 OS](https://ko.wikipedia.org/wiki/%ED%8C%9C_OS "팜 OS")CR[코모도어 8비트 머신](https://ko.wikipedia.org/w/index.php?title=%EC%BD%94%EB%AA%A8%EB%8F%84%EC%96%B4_8%EB%B9%84%ED%8A%B8_%EB%A8%B8%EC%8B%A0&action=edit&redlink=1 "코모도어 8비트 머신 (없는 문서)"), [TRS-80](https://ko.wikipedia.org/w/index.php?title=TRS-80&action=edit&redlink=1 "TRS-80 (없는 문서)"), [애플 II](https://ko.wikipedia.org/wiki/%EC%95%A0%ED%94%8C_II "애플 II"), [맥 OS](https://ko.wikipedia.org/wiki/%EB%A7%A5_OS "맥 OS") (버전 9 이하), [OS-9](https://ko.wikipedia.org/w/index.php?title=OS-9&action=edit&redlink=1 "OS-9 (없는 문서)")

---

```python
from googletrans import Translator
```

google 번역을 사용하기 위해서는 google api 에 등록하여 키도 받고 여러가지 설정을 해야 하므로 귀찮은 과정이 있는데, github 에서 검색하여 googletrans 라는 모듈을 사용하기로 하자.

설치는 pip install googletrans, 사용은 깃허브를 참고하자. <https://github.com/ssut/py-googletrans>

```python
tr = Translator()
translated = []
for line in lines:
    temp = tr.translate(line, src='en', dest='ko')
    translated.append(line)
    translated.append(temp.text)
```

검토 및 편집의 편이를 위해서 줄 단위로 번역을 했다. line 은 원문이고 temp.text 는 번역문이다. 잘 되었는지 출력을 해보니 아래와 같이 저장된다.

```python
print(translated[10:13])
```

```
['When caring for the geriatric population consideration must be given to the physiological, anatomical, and hormonal shifts related to aging in approaching the emergency complications of illness or injury of the genital and urinary systems. Special attention should be paid to the challenges of obtaining a complete and relevant history and physical of the genital and renal systems in the aged. It can be more difficult to achieve these goals in the hustle of the busy emergency department (ED), but with forethought these goals can be met.', '노인 인구를 돌보는 경우 생식기계 및 비뇨기 계통의 질병 또는 상해의 응급 합병증에 접근 할 때 노화와 관련된 생리 학적, 해부학 적 및 호르몬 변화를 고려해야합니다. 고령자의 생식기 및 신장 시스템에 대한 완전하고 관련있는 병력 및 신체 검사를 얻으려는 시도에 특별한주의를 기울여야한다. 바쁜 응급실 (ED)의 소동 속에서 이러한 목표를 달성하기가 더 어려울 수 있지만, 이러한 목표를 달성하기 위해서는 사전 계획을 세워야합니다.']
```

```python
with open("output.txt", "w") as output:
    output.writelines( "%s\n" % line for line in translated )
```

translated 는 최종적으로 원문-번역문-원문-번역문 순서대로 저장된 리스트이다. output.txt 로 저장시켜서 완성이다.