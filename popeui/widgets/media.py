from .base import BaseElement, BaseContainer
from .abstract import ViewLink


class Image(BaseElement):
  """
  A simple image widget.
  """

  html_tag = "img"

  def __init__(self, id, img_url, classname=None, parent=None):
    self.img_url = img_url
    super(Image, self).__init__(id, classname, parent)

  def _build(self):
    self.attributes["src"] = self.img_url


class Video(BaseElement):
  """
  A simple video widget, set via ``Video.attributes`` to loop by default.
  """

  html_tag = "video"

  def __init__(self, id, vid_url, classname=None, parent=None):
    self.vid_url = vid_url
    super(Video, self).__init__(id, classname, parent)

  def _build(self):
    self.attributes["src"] = self.vid_url
    self.attributes["loop"] = "true"


class ImageLink(BaseContainer):
  """
  An image widget, with the added feature of linking to an external URL.
  """

  html_tag = "a"

  def __init__(self, id, link, img_url, classname=None, parent=None):
    self.link = link
    self.img_url = img_url
    super(ImageLink, self).__init__(id, classname, parent)
    self.add_child(Image(self.attributes['id'] + '-img', self.img_url))

  def _build(self):
    self.attributes['href'] = self.link


class Audio(BaseElement):
  """
  A simple audio widget.
  """

  html_tag = "audio"

  def __init__(self, id, audio_path, classname=None, parent=None):
    self.audio_path = audio_path
    super(Audio, self).__init__(id, classname, parent)

  def _build(self):
    self.attributes["src"] = self.audio_path


class ViewImageLink(ViewLink):
  """
  An image widget, with the added feature of linking to another view
  """

  def __init__(self, id, img_url, view_name, params=None, classname=None, parent=None):
    self.img_url = img_url
    self.view_name = view_name
    self.params = params
    super(ViewImageLink, self).__init__(id=view_name, view_name=view_name, params=params, parent=parent)
    self.add_child(Image(self.attributes['id'] + '-img', self.img_url, classname=self.attributes.get('class')))


class ViewVideoLink(ViewLink):
  """
  A video widget, with the added feature of linking to another view.
  """

  def __init__(self, id, vid_url, view_name, params=None, classname=None, parent=None):
    self.vid_url = vid_url
    self.view_name = view_name
    self.params = params
    super(ViewVideoLink, self).__init__(id=view_name, view_name=view_name, params=params, parent=parent)
    self.add_child(Video(self.attributes['id'], self.vid_url, classname=self.attributes.get('class')))
