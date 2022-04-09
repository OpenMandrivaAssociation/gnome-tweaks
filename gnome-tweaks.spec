%define url_ver %(echo %{version} | cut -d "." -f -2)

Name:			gnome-tweaks
Version:		42
Release:		0.beta.0
Summary:		Tool to customize advanced GNOME 3 options
Group:			Graphical desktop/GNOME
License:		GPLv3
URL:			https://wiki.gnome.org/GnomeTweakTool
Source0:		https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.beta.tar.xz

BuildRequires:		meson
BuildRequires:		gettext
BuildRequires:		pkgconfig(gsettings-desktop-schemas)
BuildRequires:		python3dist(pygobject)
BuildRequires:		pkgconfig(gtk+-3.0)
BuildRequires:		pkgconfig(python)
Requires:		python3dist(pygobject)
Requires:		gnome-shell
Requires:   gnome-shell-extensions

#Typelib generator is broken. Add here gir package manually.
Requires: typelib(Soup)
Requires: typelib(Pango)
Requires: typelib(Notify)
Requires: typelib(Gtk)
Requires: typelib(GnomeDesktop)
Requires: typelib(Gio)
Requires: typelib(Gdk)
Requires: typelib(GObject)
Requires: typelib(GLib)
Requires: typelib(Handy)


BuildArch:		noarch
#Old tweak tool is obsoletes.
Obsoletes:		gnome-tweak-tool

%description
GNOME Tweak Tool - application for changing the advanced settings
of GNOME 3.

Features:
* Install and switch gnome-shell themes
* Switch GTK+ themes
* Switch icon themes
* Change
  - The user-interface and title bar fonts
  - Icons in menus and buttons
  - Behavior on laptop lid close
  - Shell font size
  - File manager desktop icons
  - Title bar click action
  - Shell clock to show date
  - Font hinting
  - Font anti-aliasing


%files -f %{name}.lang
# License not included in source
%doc AUTHORS NEWS README.md
%license LICENSES/*
%{_bindir}/%{name}
%{python_sitelib}/gtweak/
%{_datadir}/applications/org.gnome.tweaks.desktop
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/*tweak*.*
%{_datadir}/metainfo/org.gnome.tweaks.appdata.xml
%{_libexecdir}/gnome-tweak-tool-lid-inhibitor
%{_datadir}/glib-2.0/schemas/*.xml

#--------------------------------------------------------------------

%prep
%autosetup -n %{name}-%{version}.beta -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}
