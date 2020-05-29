# QScreenCast
A complete screen-caster behind a QToolButton

# Known issues

We need some 'services' from Qt, and it turns out that a same release doesn't implement the same things on differnt OS'es

| Qt | 5.9.2 | 5.12.3 | 5.14 | 5.15 |
|:----:|:------:|:-------:|:-------:|:-------:|
| **Channel** | anaconda | conda-forge | PIP | Qt 5.15 |
|Windows| ✗¹ | ✓ | ✓ | ? |
|Linux| ✗ | ?¹ | ✓ | ? |
|MacOS| ✗ | ? | ? | ? |

²³

Notes:
  * ✗ : does not work
  * ✓ : works
  * ? : not tested yet
  * ✗¹ : Complaining about availability of QMultiMedia, we need that to record the audio
  * ?¹ : Not complaining about QMultiMedia but complaining about codecs ... need to see if I can install the codecs.


```shell
conda install ffmpeg
```
