import gi  # 导入Gi
gi.require_version("Gtk", "3.0")  # 设置Gtk版本
from gi.repository import Gtk  # 导入Gtk


class PictureViewer(object):
    def __init__(self):
        self.Window = Gtk.Window(title="图片查看器")  # 初始化窗口
        self.Window.set_icon_name("applications-graphics")  # 设置窗口图标
        self.Window.set_default_size(780, 425)  # 设置窗口默认大小
        self.Window.set_position(Gtk.WindowPosition.CENTER_ALWAYS)  # 设置窗口位置 CENTER_ALWAYS 为窗口显示时刷新在桌面中央
        self.ClipBoard = Gtk.Clipboard()

    def OpenConfigureDialog(self, Widget):
        self.ConfigureDialog = Gtk.Window(transient_for=self.Window)
        self.ConfigureDialog.set_icon_name("applications-graphics")
        self.ConfigureDialog.set_default_size(540, 230)
        self.ConfigureDialog.set_position(Gtk.WindowPosition.CENTER_ON_PARENT)
        ######################
        self.ConfigureDialogHeaderBar = Gtk.HeaderBar()
        self.ConfigureDialogHeaderBar.set_title("图片查看器 配置")
        self.ConfigureDialogHeaderBar.set_show_close_button(True)
        self.ConfigureDialog.set_titlebar(self.ConfigureDialogHeaderBar)
        ######################
        self.ConfigureDialogIcon = Gtk.Image()  # 初始化打开文件窗口标题栏的图标
        self.ConfigureDialogIcon.set_margin_start(5)
        self.ConfigureDialogIcon.set_from_icon_name("applications-graphics", Gtk.IconSize.LARGE_TOOLBAR)  # 设置打开文件窗口标题栏的图标
        self.ConfigureDialogHeaderBar.pack_start(self.ConfigureDialogIcon)  # 打开文件窗口的标题栏加入图片组件
        ######################
        self.ConfigureDialogNoteBook = Gtk.Notebook()

        self.ConfigureDialogOperation = Gtk.Grid()
        self.ConfigureDialogOperationCilp = Gtk.Label(label="选择完图片后复制到剪切板上：")
        self.ConfigureDialogOperationCheck = Gtk.CheckButton(label="确定")
        self.ConfigureDialogOperation.attach(self.ConfigureDialogOperationCilp, 0, 0, 1, 1)
        self.ConfigureDialogOperation.attach(self.ConfigureDialogOperationCheck, 1, 0, 1, 1)
        self.ConfigureDialogOperationLabel = Gtk.Label(label="操作")
        self.ConfigureDialogNoteBook.append_page(self.ConfigureDialogOperation, self.ConfigureDialogOperationLabel)
        self.ConfigureDialog.add(self.ConfigureDialogNoteBook)
        ######################
        self.ConfigureDialog.show_all()

    def OpenChooserPictureDialog(self, Widget):
        self.ChooserPictureDialog = Gtk.Window(transient_for=self.Window)  # 初始化打开图片文件的窗口
        self.ChooserPictureDialog.set_icon_name("applications-graphics")
        self.ChooserPictureDialog.set_default_size(540, 230)
        self.ChooserPictureDialog.set_position(Gtk.WindowPosition.CENTER_ON_PARENT)

        self.ChooserPictureDialogLayout = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.ChooserPictureDialog.add(self.ChooserPictureDialogLayout)

        self.ChooserPictureDialogHeaderBar = Gtk.HeaderBar()  # 初始化打开文件窗口的标题栏
        self.ChooserPictureDialogHeaderBar.set_title("请选择一个图片文件")
        self.ChooserPictureDialogHeaderBar.set_show_close_button(True)  # 设置显示标题栏的按钮

        self.ChooserPictureDialogIcon = Gtk.Image()  # 初始化打开文件窗口标题栏的图标
        self.ChooserPictureDialogIcon.set_margin_start(5)
        self.ChooserPictureDialogIcon.set_from_icon_name("applications-graphics", Gtk.IconSize.LARGE_TOOLBAR)  # 设置打开文件窗口标题栏的图标
        self.ChooserPictureDialogHeaderBar.pack_start(self.ChooserPictureDialogIcon)  # 打开文件窗口的标题栏加入图片组件

        self.ChooserPictureDialogHeaderBarOK = Gtk.Button(label="选择")
        self.ChooserPictureDialogHeaderBarOK.connect("clicked", self.OpenChooserPictureDialogOK)
        self.ChooserPictureDialogHeaderBar.pack_end(self.ChooserPictureDialogHeaderBarOK)

        self.ChooserPictureDialogHeaderBarCanel = Gtk.Button(label="取消")
        self.ChooserPictureDialogHeaderBarCanel.connect("clicked", self.OpenChooserPictureDialogCanel)
        self.ChooserPictureDialogHeaderBar.pack_end(self.ChooserPictureDialogHeaderBarCanel)

        self.ChooserPictureDialog.set_icon_name("applications-graphics")
        self.ChooserPictureDialog.set_titlebar(self.ChooserPictureDialogHeaderBar)

        self.ChooserPictureWidget = Gtk.FileChooserWidget(action=Gtk.FileChooserAction.OPEN)
        self.ChooserPictureWidget.set_show_hidden(True)
        self.ChooserPictureWidget.set_do_overwrite_confirmation(True)
        self.ChooserPictureWidget.set_create_folders(True)
        self.ChooserPictureDialogLayout.pack_start(self.ChooserPictureWidget, True, True, 0)

        self.ChooserPictureDialog.show_all()

    def OpenChooserPictureDialogOK(self, Widget):
        self.Path = self.ChooserPictureWidget.get_file()
        if not self.Path:
            return
        self.PicturePageImage.set_from_file(self.Path.get_path())
        self.PicturePageImagePathText.set_text(self.Path.get_path())
        self.HeaderBar.set_subtitle(self.Path.get_basename())
        if self.ConfigureDialogOperationCheck.get_active():
            self.ClipBoard.set_text(self.Path.get_path(), 0)
        print(self.Path.get_path())
        print(self.Path.get_basename())
        self.OpenChooserPictureDialogCanel(self.ChooserPictureDialogHeaderBarOK)

    def OpenChooserPictureDialogCanel(self, Widget):
        self.ChooserPictureDialog.close()

    def CreatorResources(self):
        pass

    def SetHeaderBar(self):
        self.HeaderBar = Gtk.HeaderBar()
        self.HeaderBar.set_title("图片查看器")
        self.HeaderBar.set_show_close_button(True)

        self.AboutButton = Gtk.Button(label="")
        self.HeaderBar.pack_end(self.AboutButton)

        self.ApplicationIcon = Gtk.Image()
        self.ApplicationIcon.set_from_icon_name("applications-graphics", Gtk.IconSize.LARGE_TOOLBAR)
        self.ApplicationButton = Gtk.Button()
        self.ApplicationButton.connect("clicked", self.OpenConfigureDialog)
        self.ApplicationButton.set_image(self.ApplicationIcon)
        self.HeaderBar.pack_start(self.ApplicationButton)

        self.Window.set_titlebar(self.HeaderBar)

    def SetLayout(self):
        self.WindowLayout = Gtk.Box(orientation=0)
        self.Window.add(self.WindowLayout)
        self.Button = Gtk.Button()

    def SetPageView(self):
        self.Page = Gtk.Stack()
        self.Page.set_transition_type(Gtk.StackTransitionType.UNDER_DOWN)
        self.Page.set_transition_duration(300)
        ###############################
        self.HomePage = Gtk.Box()
        self.HomePageChooserButton = Gtk.Button(label="选择图片")
        self.HomePageChooserButton.connect("clicked", self.OpenChooserPictureDialog)
        self.HomePage.pack_start(self.HomePageChooserButton, True, True, 0)
        self.Page.add_titled(self.HomePage, "home", "首页")
        ###############################
        self.PicturePageScoll = Gtk.ScrolledWindow()
        self.PicturePage = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.PicturePageImage = Gtk.Image()
        self.PicturePageImage.set_from_icon_name("applications-graphics", Gtk.IconSize.DIALOG)
        self.PicturePage.pack_start(self.PicturePageImage, True, True, 5)

        self.PicturePageImagePathScroll = Gtk.ScrolledWindow()
        self.PicturePageImagePath = Gtk.TextView()
        self.PicturePageImagePathText = Gtk.TextBuffer()
        self.PicturePageImagePathText.set_text("无图片")
        self.PicturePageImagePath.set_buffer(self.PicturePageImagePathText)
        self.PicturePageImagePath.set_editable(False)
        self.PicturePageImagePathScroll.add(self.PicturePageImagePath)

        self.PicturePage.pack_end(self.PicturePageImagePathScroll, False, False, 5)
        self.PicturePage.pack_end(self.PicturePageImage, True, False, 5)
        self.PicturePageScoll.add(self.PicturePage)
        self.Page.add_titled(self.PicturePageScoll, "picture", "图片")
        ###############################
        self.SideBar = Gtk.StackSidebar()
        self.SideBar.set_stack(self.Page)
        self.WindowLayout.pack_start(self.SideBar, False, False, 0)
        self.WindowLayout.pack_start(self.Page, True, True, 1)

    def SetUp(self):
        self.SetHeaderBar()
        self.SetLayout()
        self.SetPageView()

    def Run(self):
        self.Window.connect("delete-event", Gtk.main_quit)
        self.Window.show_all()
        Gtk.main()


def Run():
    Root = PictureViewer()
    Root.SetUp()
    Root.Run()


if __name__ == '__main__':
    Run()
