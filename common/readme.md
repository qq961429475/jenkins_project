# 在html中嵌入图片

```python
with open("tt.png", "rb") as image_file:
    image_data = image_file.read()
    image = MIMEImage(image_data, _subtype='png')
    image.add_header("Content-ID", "<image1>")
    message.attach(image)

html_content = """
         <html>
          <body>
            <p>你好, 世界!</p>
            <!-- 使用占位符IMAGE_PLACEHOLDER来插入图片 -->
            <p>这是一封包含图片的HTML邮件：</p>
            <p>IMAGE_PLACEHOLDER</p>
          </body>
        </html>
        """
html_content_with_image = html_content.replace('IMAGE_PLACEHOLDER',
                                               '<img src="cid:image1" alt="Embedded Image" />')

message.attach(MIMEText(html_content_with_image, "html"))

```