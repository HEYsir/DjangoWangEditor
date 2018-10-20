# wangEditor-django
### 使用方法:
进入项目根目录，将项目文件放到项目根目录

####接下来进行设置相关配置

将`DjangoWangEditor`添加进项目的`INSTALLED_APPS`下面

```
INSTALLED_APPS = [
    ...

    'DjangoWangEditor',
    
    ...
]
```

然后继续在该`settings.py`文件中添加设置`MEDIA_ROOT`如:

```
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

####注：编辑器上传的图片将存放在MEDIA_ROOT下的upload文件夹,如需存放到其他文件夹自行修改本项目下的`views.py`相关代码和`settings.py`的OUTPUT_PATH
<br />

然后在`urls.py`的`urlpatterns`中添加一行
```
url(r'^wangeditor/', include('DjangoWangEditor.urls')),
```

####这样基本就完成了
使用该编辑器只需将你的项目原本定义的TextField更改成WangEditorField即可

WangEditorField通过下面代码引入

```
from DjangoWangEditor.models import WangEditorField
```

####编辑器的初始化配置等信息在本项目下的templates/wangeditor.html