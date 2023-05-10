"""
- Explain what does django-admin.py make messages command is used for? 

- When building a multilingual website or application, it's important to provide translations for all text 
  displayed to users. Django provides a built-in translation framework that allows developers to mark strings 
  in their source code as "translatable" and provide translations for those strings in various languages.

  The make-messages command is used to scan a project's source code and extract any translatable strings marked
  with the gettext function or its alias _(). It then creates message files in the specified languages (or all 
  languages if no specific languages are specified) that contain those strings as well as other metadata such as
  the source file location and context.

  After the message files are created, translators can use tools like gettext to provide translations for the
  extracted strings. Once translations are complete, the compilemessages command can be used to compile the
  translated message files into binary format for use by the application.
"""