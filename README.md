# twitter-example

Bounded Context와 Domain Event를 연습해보기 위해 파이썬으로 예제를 만들어 보았습니다. 간단한 DI 컨테이너를 사용합니다.

## Domain Event 발행-처리 구현

분리된 맥락간에 도메인 이벤트를 발행하고 처리하기 위해 다음과 같은 도구를 `twitter.common.event` 패키지에 작성했습니다.

- Event (이벤트 객체)
- EventDispatcher (이벤트와 이벤트 핸들러를 이어주기 위한 객체)
- EventHandler (발행된 이벤트를 처리하기 위한 객체)

이 때, Event 객체를 생성하고 EventDispatcher로 넘겨주는 작업은 집합체에서 진행하게 됩니다. 코드는 `twitter.common.entity.Aggregate`에 작성했습니다.
