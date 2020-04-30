from django.shortcuts import render


def index(request):
    return render(request, 'whattolearn/index.html')


def forwhat(request):
    return render(request, 'whattolearn/forwhat/index.html')


def robot(request):
    return render(request, 'whattolearn/forwhat/robot/index.html')


def data(request):
    return render(request, 'whattolearn/forwhat/data/index.html')


def platform(request):
    return render(request, 'whattolearn/forwhat/comp/index.html')


def windows(request):
    return render(request, 'whattolearn/forwhat/comp/windows/index.html')


def macintosh(request):
    return render(request, 'whattolearn/forwhat/comp/macintosh/index.html')


def pc_console(request):
    return render(request, 'whattolearn/forwhat/comp/pc_console/index.html')


def web(request):
    return render(request, 'whattolearn/forwhat/web/index.html')


def frontend(request):
    return render(request, 'whattolearn/forwhat/web/front-end/index.html')


def backend(request):
    return render(request, 'whattolearn/forwhat/web/backend/index.html')


def freelance(request):
    return render(request, 'whattolearn/forwhat/web/backend/freelance/index.html')


def startup(request):
    return render(request, 'whattolearn/forwhat/web/backend/startup/index.html')


def company(request):
    return render(request, 'whattolearn/forwhat/web/backend/company/index.html')


def mobile(request):
    return render(request, 'whattolearn/forwhat/mobile/index.html')


def apple(request):
    return render(request, 'whattolearn/forwhat/mobile/apple/index.html')


def android(request):
    return render(request, 'whattolearn/forwhat/mobile/android/index.html')


def games(request):
    return render(request, 'whattolearn/forwhat/games/index.html')


def web_game(request):
    return render(request, 'whattolearn/forwhat/games/web_game/index.html')


def virtual(request):
    return render(request, 'whattolearn/forwhat/games/virtual/index.html')


def pcconsole(request):
    return render(request, 'whattolearn/forwhat/games/pc_console/index.html')


def simple_game(request):
    return render(request, 'whattolearn/forwhat/games/pc_console/simple-game/index.html')


def gamespc(request):
    return render(request, 'whattolearn/forwhat/games/pc_console/games/index.html')


def gamemob(request):
    return render(request, 'whattolearn/forwhat/games/mobile/index.html')


def twoD(request):
    return render(request, 'whattolearn/forwhat/games/mobile/2D/index.html')


def threeD(request):
    return render(request, 'whattolearn/forwhat/games/mobile/3D/index.html')
# Create your views here.
