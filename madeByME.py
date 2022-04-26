from tkinter import *;
from tkinter import font,colorchooser,filedialog,messagebox;
import os;

from tkinter.ttk import Combobox;
window = Tk();
window.title("Code Code and Code...");
window.geometry("1280x720+0+0");
menu = Menu(window);
# *******************************************************************************************************
current_font_family='Arial';
current_font_size=14;
current_font_weight="normal";
current_font_slant="roman";
current_font_underline='normal'
url="";
show_toolbar=BooleanVar();
show_toolbar.set(True);
show_statusbar=BooleanVar();
show_statusbar.set(True);
# .......................................................................................................
# *******************************************************************************************************
file=Menu(menu,tearoff=0);
view=Menu(menu,tearoff=0);
themes=Menu(menu,tearoff=0);
edit=Menu(menu,tearoff=0);
# .......................................................................................................
new_file_icon = PhotoImage(file=r"icons1\new.png");
open_file_icon=PhotoImage(file=r"icons1\open.png");
save_icon=PhotoImage(file=r"icons1\save.png");
save_as_icon=PhotoImage(file=r"icons1\save_as.png");
exit_icon=PhotoImage(file=r"icons1\exit.png");
def new_file(event=None):
    global url;
    url="";
    textarea.delete(1.0,END);
file.add_command(label="New",image=new_file_icon,compound=LEFT,accelerator="Ctrl+n",command=new_file);
def open_file(event=None):
    global url;
    url=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select File",filetypes=(('All Files',"*.*"),('Text Files','*.txt')));
    try:
        with open(url,'r') as f:
            textarea.delete(1.0,END);
            textarea.insert(1.0,f.read());
    except FileNotFoundError:
        return;
    except:
        return;
    window.title(os.path.basename(url))
file.add_command(label="Open",image=open_file_icon,compound=LEFT,accelerator="Ctrl+o",command=open_file);
file.add_separator();
def save_file(event=None):
    global url;
    try:
        if url:
            content=str(textarea.get(1.0,END));
            with open(url,'w',encoding='utf-8') as f:
                f.write(content);
        else:
            url=filedialog.asksaveasfile(mode="w",defaultextension=".txt",filetypes=(("All Files","*.*"),("Text Files","*.txt")));
            content=textarea.get(1.0,END);
            url.write(content);
            url.close();
    except:
        return;
file.add_command(label="Save",image=save_icon,compound=LEFT,accelerator="Ctrl+s",command=save_file);
def save_as_file(event=None):
    global url;
    try:
        content=textarea.get(1.0,END);
        url=filedialog.asksaveasfile(mode="w",defaultextension=".txt",filetypes=(('All Files','*.*'),("Text Files",'*.txt')));
        url.write(content);
        url.close();
    except:
        return;
file.add_command(label="Save As",image=save_as_icon,compound=LEFT,accelerator="Ctrl+Alt+s",command=save_as_file);
file.add_separator();
def exit(event=None):
    global url,text_modified;
    try:
        if text_modified:
            choice = messagebox.askyesnocancel('Save File',"Do you want to save the file??");
            if choice is True:
                if url:
                    content=textarea.get(1.0,END);
                    with open(url,'w',encoding="utf-8") as f:
                        f.write(content);
                        window.destroy();
                else:
                    content=textarea.get(1.0,END);
                    url=filedialog.asksaveasfile(mode="w",defaultextension=".txt",filetypes=(("All Files","*.*"),("Text Files","*.txt")));
                    url.write(content);
                    url.close();
                    window.destroy();
            elif choice is False:
                window.destroy();
        else:
            window.destroy();
    except:
        return;
file.add_command(label="Exit",image=exit_icon,compound=LEFT,accelerator="Ctrl+q",command=exit);
# .......................................................................................................

# *******************************************************************************************************
copy_icon = PhotoImage(file=r"icons1\copy.png");
paste_icon= PhotoImage(file=r"icons1\paste.png");
cut_icon= PhotoImage(file=r"icons1\cut.png");
find_icon=PhotoImage(file=r"icons1\find.png");
clear_all_icon=PhotoImage(file=r"icons1\clear_all.png");
edit.add_command(label="Copy",image=copy_icon,compound=LEFT,accelerator="Ctrl+c",command=lambda:textarea.event_generate("<Control c>"));
edit.add_command(label="Paste",image=paste_icon,compound=LEFT,accelerator="Ctrl+p",command=lambda:textarea.event_generate("<Control v>"));
edit.add_command(label="Cut",image=cut_icon,compound=LEFT,accelerator="Ctrl+x",command=lambda:textarea.event_generate("<Control x>"));
def clear_all(event=None):
    textarea.delete(1.0,END);
edit.add_command(label="Clear All",image=clear_all_icon,compound=LEFT,accelerator="Ctrl+Alt+c",command=clear_all);
def find_replace(event=None):
    def find_func(event=None):
        word=find_inpt.get();
        textarea.tag_remove('catch',1.0,END);
        if word:
            start_pos='1.0';
            while True:
                start_pos=textarea.search(word,start_pos,stopindex=END);
                if not start_pos:
                    break;
                end_pos=f"{start_pos}+{len(word)}c";
                textarea.tag_add('catch',start_pos,end_pos);
                start_pos=end_pos;
                textarea.tag_config('catch',foreground="#fff",background="#000")
    def replace_func(event=None):
        word = find_inpt.get();
        replace_word = replace_inpt.get();
        content=textarea.get(1.0,END);
        new_content=content.replace(word,replace_word);
        textarea.delete(1.0,END);
        textarea.insert(1.0,new_content);
    top = Toplevel(window,bg="#ff01b3");
    top.title("Find/Replace");
    top.geometry('400x250+400+250');
    top.focus_set();
    label_frame = LabelFrame(top,relief=GROOVE,bg='#ff01b3',bd=3,font=('Consolas',14,'bold'),text="Find/Replace",width=100,height=100);
    label_frame.grid(row=0,column=0,padx=20,pady=20,ipadx=10,ipady=10);
    l1=Label(label_frame,bg='#ff01b3',text='Find         : ',font=("arial",12,'bold'));
    l1.grid(row=0,column=0,padx=20,pady=10,sticky=W);
    find_inpt=StringVar();
    l1_entry=Entry(label_frame,textvariable=find_inpt,bg="#ffa9e5",fg='#000',width=20,font=('san-serif',13,'bold'));
    l1_entry.focus();
    l1_entry.grid(row=0,column=1,padx=8,pady=8,ipadx=2,ipady=2,sticky=W)
    l2=Label(label_frame,bg='#ff01b3',text='Replace  : ',font=("arial",12,'bold'));
    l2.grid(row=1,column=0,padx=20,pady=10,sticky=W);
    replace_inpt = StringVar();
    l2_entry=Entry(label_frame,textvariable=replace_inpt,bg="#ffa9e5",fg='#000',width=20,font=('san-serif',13,'bold'));
    l2_entry.grid(row=1,column=1,padx=8,pady=8,ipadx=2,ipady=2,sticky=W)
    btn_find=Button(label_frame,command=find_func,activebackground="#8a2be2",activeforeground="#fff",bg="gray",fg="#fff",text='Find',font=('Consolas',13,'bold'));
    btn_find.grid(row=3,column=0,padx=30,pady=10,ipadx=15);
    btn_replace=Button(label_frame,command=replace_func,activebackground="#8a2be2",activeforeground="#fff",bg="gray",fg="#fff",text='Replace',font=('Consolas',13,'bold'));
    btn_replace.grid(row=3,column=1,padx=30,pady=10,ipadx=15);
edit.add_command(label="Find",image=find_icon,compound=LEFT,accelerator="Ctrl+F",command=find_replace);
# .......................................................................................................

# *******************************************************************************************************
toolbar_icon = PhotoImage(file=r"icons1\tool_bar.png");
statusbar_icon = PhotoImage(file=r"icons1\status_bar.png");
def toggle_toolbar():
    global show_toolbar,show_statusbar;
    if show_toolbar:
        toolbar.pack_forget();
        show_toolbar=False;
    else:
        textarea.pack_forget();
        statusbar.pack_forget();
        toolbar.pack(fill=X);
        textarea.pack(expand=True,fill=BOTH);
        if show_statusbar:
            statusbar.pack(side=BOTTOM,fill=X);
        show_toolbar=True;
def toggle_statusbar():
    global show_statusbar;
    if show_statusbar:
        statusbar.pack_forget();
        show_statusbar=False;
    else:
        statusbar.pack(side=BOTTOM,fill=X);
        show_statusbar=True;
view.add_checkbutton(label="Toolbar",image=toolbar_icon,compound=LEFT,command=toggle_toolbar,variable=show_toolbar);
view.add_checkbutton(label="Statusbar",image=statusbar_icon,compound=LEFT,command=toggle_statusbar,variable=show_statusbar);
# .......................................................................................................

# *******************************************************************************************************
theme_choosed=StringVar();
lightplus_icon = PhotoImage(file=r"icons1\light_plus.png");
lightdefault_icon = PhotoImage(file=r"icons1\light_default.png");
monokai_icon = PhotoImage(file=r"icons1\monokai.png");
nightblue_icon = PhotoImage(file=r"icons1\night_blue.png");
dark_icon = PhotoImage(file=r"icons1\dark.png");
red_icon = PhotoImage(file=r"icons1\red.png");
color_themes_icon=(lightdefault_icon,lightplus_icon,dark_icon,red_icon,monokai_icon,nightblue_icon);
color_dict={
    'Lightdefault':('#000','#fff'),
    'Lightplus':('#2d2d2d','#ffe8ff'),
    'Dark':('#ffffff','#000000'),
    'Red':('#474747','#e0e0e0'),
    'Monokai':('#d3b774','#474747'),
    'Night Blue':('#ededed','#5b9db2')
}
def change_theme():
    theme=theme_choosed.get();
    theme_choose=color_dict.get(theme);
    textarea.configure(fg=theme_choose[0],bg=theme_choose[1])
count=0;
for i in color_dict:
    themes.add_radiobutton(label=i,compound=LEFT,image=color_themes_icon[count],command=change_theme,variable=theme_choosed)
    count+=1;
# .......................................................................................................
# *******************************************************************************************************
menu.add_cascade(menu=file,label="File");
menu.add_cascade(menu=edit,label="Edit");
menu.add_cascade(menu=view,label="View");
menu.add_cascade(menu=themes,label="Themes");
# .......................................................................................................

# *******************************************************************************************************
toolbar = Label(window,background="#af9");
toolbar.pack(fill=X);
# .......................................................................................................

# *******************************************************************************************************

textarea=Text(window);
textarea.config(wrap="word",relief=FLAT);
scroll_x = Scrollbar(window);
scroll_x.pack(side=RIGHT,fill=Y);
textarea.focus_set();
textarea.pack(expand=True,fill=BOTH);
scroll_x.config(command=textarea.yview);
textarea.config(yscrollcommand=scroll_x.set);
textarea.configure(font=(current_font_family,current_font_size))
# .......................................................................................................

# *******************************************************************************************************
def font_family_func(event=None):
    global current_font_family;
    current_font_family=font_family_name.get();
    textarea.configure(font=(current_font_family,current_font_size))
font_families = font.families();
font_family_name=StringVar();
c1 = Combobox(toolbar,width=35,textvariable=font_family_name,state="readonly",font=("Consolas",10));
c1['values']=font_families;
c1.current(font_families.index('Arial'));
c1.grid(row=0,column=0,padx=2,sticky=W,pady=0);
c1.bind("<<ComboboxSelected>>",font_family_func);
# .......................................................................................................

# *******************************************************************************************************
def font_size_func(event=None):
    global current_font_size;
    current_font_size=font_size.get();
    textarea.configure(font=(current_font_family,current_font_size));
font_size_tuple=tuple(range(2,82,2));
font_size=StringVar();
c2=Combobox(toolbar,width=10,state="readonly",textvariable=font_size,font=("Consolas",10));
c2['values']=font_size_tuple;
c2.current(font_size_tuple.index(14));
c2.grid(row=0,column=1,padx=3,pady=0,sticky=W);
c2.bind("<<ComboboxSelected>>",font_size_func);
# .......................................................................................................

# *******************************************************************************************************
def bold_func(event=None):
    global current_font_weight,current_font_slant,current_font_underline;
    text_property=font.Font(font=textarea['font']);
    if text_property.actual()['weight']=="normal":
        current_font_weight='bold'
        textarea.config(font=(current_font_family,current_font_size,current_font_weight,current_font_slant));
    else:
        current_font_weight='normal'
        textarea.config(font=(current_font_family,current_font_size,current_font_weight,current_font_slant));

bold_icons=PhotoImage(file=r"icons1\bold.png");
btn1=Button(toolbar,image=bold_icons,relief=GROOVE,command=bold_func);
btn1.grid(row=0,column=2,padx=3);
# .......................................................................................................

# *******************************************************************************************************
def italic_func(event=None):
    global current_font_weight,current_font_slant,current_font_underline
    text_property=font.Font(font=textarea['font']);
    if text_property.actual()['slant']=='roman':
        current_font_slant='italic'
        textarea.config(font=(current_font_family,current_font_size,current_font_weight,current_font_slant))
    else:
        current_font_slant='roman';
        textarea.config(font=(current_font_family,current_font_size,current_font_weight,current_font_slant))
italic_icons=PhotoImage(file=r"icons1\italic.png");
btn2=Button(toolbar,image=italic_icons,relief=GROOVE,command=italic_func);
btn2.grid(row=0,column=3,padx=3);
# .......................................................................................................

# *******************************************************************************************************
def underline_func(event=None):
    global current_font_weight,current_font_slant,current_font_underline;
    text_property=font.Font(font=textarea['font']);
    if text_property.actual()['underline'] ==0:
        current_font_underline='underline';
        textarea.config(font=(current_font_family,current_font_size,current_font_weight,current_font_slant,current_font_underline))
    else:
        current_font_underline='normal';
        textarea.config(font=(current_font_family,current_font_size,current_font_weight,current_font_slant,current_font_underline))

underline_icons=PhotoImage(file=r"icons1\underline.png");
btn1=Button(toolbar,image=underline_icons,relief=GROOVE,command=underline_func);
btn1.grid(row=0,column=4,padx=3);
# .......................................................................................................

# *******************************************************************************************************
def left_align_func(event=None):
    content = textarea.get(1.0,END);
    textarea.tag_config('left',justify=LEFT);
    textarea.delete(1.0,END);
    textarea.insert(INSERT,content,LEFT);
align_left_icons=PhotoImage(file=r"icons1\align_left.png");
btn1=Button(toolbar,image=align_left_icons,relief=GROOVE,command=left_align_func);
btn1.grid(row=0,column=6,padx=3);  
# .......................................................................................................
# *******************************************************************************************************
def center_align_func(event=None):
    content=textarea.get(1.0,END);
    textarea.tag_config('center',justify=CENTER);
    textarea.delete(1.0,END);
    textarea.insert(INSERT,content,CENTER);
align_center_icons=PhotoImage(file=r"icons1\align_center.png");
btn1=Button(toolbar,image=align_center_icons,relief=GROOVE,command=center_align_func);
btn1.grid(row=0,column=7,padx=3);
# .......................................................................................................
# *******************************************************************************************************
def right_align_func(event=None):
    content=textarea.get(1.0,END);
    textarea.tag_config('right',justify=RIGHT)
    textarea.delete(1.0,END);
    textarea.insert(INSERT,content,RIGHT)
align_right_icons=PhotoImage(file=r"icons1\align_right.png");
btn1=Button(toolbar,image=align_right_icons,relief=GROOVE,command=right_align_func);
btn1.grid(row=0,column=8,padx=3);
# .......................................................................................................
# *******************************************************************************************************
def choose_color(event=None):
    color_var = colorchooser.askcolor();
    textarea.config(fg=color_var[1]);

font_color_icons=PhotoImage(file=r"icons1\font_color.png");
btn1=Button(toolbar,image=font_color_icons,relief=GROOVE,command=choose_color);
btn1.grid(row=0,column=9,padx=3);
# .......................................................................................................
# *******************************************************************************************************
statusbar = Label(window,text="Status bar");
statusbar.pack(side=BOTTOM,fill=X)
text_modified = False;
def changed(event=None):
    global text_modified;
    if textarea.edit_modified():
        text_modified=True;
        words=len(textarea.get(1.0,END).split());#"ende-1c"
        charactors=len(textarea.get(1.0,END));
        statusbar.configure(text=f"Charactor : {charactors} | Words : {words}");
    textarea.edit_modified(False);
textarea.bind("<<Modified>>",changed);
# .......................................................................................
window.bind('<Control n>',new_file);
window.bind('<Control o>',open_file);
window.bind('<Control s>',save_file);
window.bind('<Control-Alt-s>',save_as_file);
window.bind('<Control q>',exit);
window.bind('<Control-Alt-c>',clear_all);
window.bind('<Control f>',find_replace);
window.config(menu=menu);
window.mainloop();