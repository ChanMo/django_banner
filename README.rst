Django-banner
=============

基于django的轮播图模块

使用方法:
---------

安装依赖模块:

.. code-block::

    pip install adminsortable2

修改 *settings.py* 文件:

.. code-block::

    INSTALLED_APPS = (
        ...
        'adminsortable2',
        'banner',
        ...
    )

添加数据表:

.. code-block::

    python manage.py migrate


版本更改:
---------
- v0.2 添加分组
- v0.1 第一版
