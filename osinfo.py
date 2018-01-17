# coding: utf-8

# Standard library imports
import platform

# External imports

# Local import
from shell import shellcmd

# global var
# 是否显示日志信息
SHOW_LOG = True

def OSInfo():
    ret = HTMLCode('目标系统信息')
    if SHOW_LOG:
        ret += show_os_all_info()
    else:
        ret += show_os_info()
    ret += HTMLPrint('- - ' * 10)
    ret += HTMLPrint('目标系统中的python信息：')
    if SHOW_LOG:
        ret += show_python_all_info()
    else:
        ret += show_python_info()

    ret += HTMLPrint('- - ' * 10)
    ret += HTMLPrint('echo $PATH')
    retshell = shellcmd('echo $PATH')
    for s in retshell:
        ret += HTMLPrint(str((s.encode('utf-8'))))

    ret += HTMLPrint('- - ' * 10)
    ret += HTMLPrint('pip list')
    retshell = shellcmd('pip list')
    for s in retshell:
        ret += HTMLPrint(str((s.encode('utf-8'))))

    ret += HTMLPrint('- - ' * 10)
    ret += HTMLPrint('python --version')
    retshell = shellcmd('python --version')
    for s in retshell:
        ret += HTMLPrint(str((s.encode('utf-8'))))

    ret += HTMLPrint('- - ' * 10)
    ret += HTMLPrint('ps aux')
    retshell = shellcmd('ps aux')
    for s in retshell:
        ret += HTMLPrint(str((s.encode('utf-8'))))

    ret += HTMLCode(None)
    return ret

def show_os_all_info():
    '''打印os的全部信息'''
    ret = HTMLPrint('获取操作系统名称及版本号 : [{}]'.format(get_platform()))
    ret += HTMLPrint('获取操作系统版本号 : [{}]'.format(get_version()))
    ret += HTMLPrint('获取操作系统的位数 : [{}]'.format(get_architecture()))
    ret += HTMLPrint('计算机类型 : [{}]'.format(get_machine()))
    ret += HTMLPrint('计算机的网络名称 : [{}]'.format(get_node()))
    ret += HTMLPrint('计算机处理器信息 : [{}]'.format(get_processor()))
    ret += HTMLPrint('获取操作系统类型 : [{}]'.format(get_system()))
    ret += HTMLPrint('汇总信息 : [{}]'.format(get_uname()))
    return ret

def show_os_info():
    '''只打印os的信息，没有解释部分'''
    ret = HTMLPrint(get_platform())
    ret += HTMLPrint(get_version())
    ret += HTMLPrint(get_architecture())
    ret += HTMLPrint(get_machine())
    ret += HTMLPrint(get_node())
    ret += HTMLPrint(get_processor())
    ret += HTMLPrint(get_system())
    ret += HTMLPrint(get_uname())
    return ret

def show_python_all_info():
    '''打印python的全部信息'''
    ret = HTMLPrint('The Python build number and date as strings : [{}]'.format(get_python_build()))
    ret += HTMLPrint(
        'Returns a string identifying the compiler used for compiling Python : [{}]'.format(get_python_compiler()))
    ret += HTMLPrint(
        'Returns a string identifying the Python implementation SCM branch : [{}]'.format(get_python_branch()))
    ret += HTMLPrint(
        'Returns a string identifying the Python implementation : [{}]'.format(get_python_implementation()))
    ret += HTMLPrint('The version of Python ： [{}]'.format(get_python_version()))
    ret += HTMLPrint('Python implementation SCM revision : [{}]'.format(get_python_revision()))
    ret += HTMLPrint('Python version as tuple : [{}]'.format(get_python_version_tuple()))
    return ret


def show_python_info():
    '''只打印python的信息，没有解释部分'''
    ret = HTMLPrint(get_python_build())
    ret += HTMLPrint(get_python_compiler())
    ret += HTMLPrint(get_python_branch())
    ret += HTMLPrint(get_python_implementation())
    ret += HTMLPrint(get_python_version())
    ret += HTMLPrint(get_python_revision())
    ret += HTMLPrint(get_python_version_tuple())
    return ret

'''
    python中，platform模块给我们提供了很多方法去获取操作系统的信息
    如：
        import platform
        platform.platform()   #获取操作系统名称及版本号，'Windows-7-6.1.7601-SP1'
        platform.version()    #获取操作系统版本号，'6.1.7601'
        platform.architecture()   #获取操作系统的位数，('32bit', 'WindowsPE')
        platform.machine()    #计算机类型，'x86'
        platform.node()       #计算机的网络名称，'hongjie-PC'
        platform.processor()  #计算机处理器信息，'x86 Family 16 Model 6 Stepping 3, AuthenticAMD'
        platform.uname()      #包含上面所有的信息汇总，uname_result(system='Windows', node='hongjie-PC',
                               release='7', version='6.1.7601', machine='x86', processor='x86 Family
                               16 Model 6 Stepping 3, AuthenticAMD')

        还可以获得计算机中python的一些信息：
        import platform
        platform.python_build()
        platform.python_compiler()
        platform.python_branch()
        platform.python_implementation()
        platform.python_revision()
        platform.python_version()
        platform.python_version_tuple()
'''

def get_platform():
    '''获取操作系统名称及版本号'''
    return platform.platform()

def get_version():
    '''获取操作系统版本号'''
    return platform.version()

def get_architecture():
    '''获取操作系统的位数'''
    return platform.architecture()


def get_machine():
    '''计算机类型'''
    return platform.machine()

def get_node():
    '''计算机的网络名称'''
    return platform.node()

def get_processor():
    '''计算机处理器信息'''
    return platform.processor()

def get_system():
    '''获取操作系统类型'''
    return platform.system()

def get_uname():
    '''汇总信息'''
    return platform.uname()

def get_python_build():
    ''' the Python build number and date as strings'''
    return platform.python_build()

def get_python_compiler():
    '''Returns a string identifying the compiler used for compiling Python'''
    return platform.python_compiler()

def get_python_branch():
    '''Returns a string identifying the Python implementation SCM branch'''
    return platform.python_branch()

def get_python_implementation():
    '''Returns a string identifying the Python implementation. Possible return values are: ‘CPython’, ‘IronPython’, ‘Jython’, ‘PyPy’.'''
    return platform.python_implementation()

def get_python_version():
    '''Returns the Python version as string 'major.minor.patchlevel'
    '''
    return platform.python_version()

def get_python_revision():
    '''Returns a string identifying the Python implementation SCM revision.'''
    return platform.python_revision()

def get_python_version_tuple():
    '''Returns the Python version as tuple (major, minor, patchlevel) of strings'''
    return platform.python_version_tuple()

def HTMLPrint(text):
    return '<p>' + text + '</p>\n'

def HTMLPrintH(text):
    return '<h2>' + text + '</h2>\n'

def HTMLCode(title):
	# 返回Html页面必要的编码
	# HTMLCode('Title') + HTMLCode(None)构成闭合的整体
	if (title):
		ret = '<html><head><meta http-equiv="Content-Type" content="text/html; charset=GBK">'
		ret += '<title>System Info</title><link rel="stylesheet" href="/static/style.css" type="text/css"></head><body><div id="container"><h1>'
		ret += title + '</h1>\n'
		return ret
	else:
		return '</div></body></html>'