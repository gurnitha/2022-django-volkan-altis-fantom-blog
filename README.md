# 2022-django-volkan-altis-fantom-blog
This is my exercise based on MyLearning on Udemy. This course made by Mr. Volkan Altis.

Github repository: https://github.com/gurnitha/2022-django-volkan-altis-fantom-blog


#### 1. Create django project

        modified:   README.md
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py


#### 2. Create django app 'blog'

        modified:   README.md
        new file:   blog/__init__.py
        new file:   blog/admin.py
        new file:   blog/apps.py
        new file:   blog/migrations/__init__.py
        new file:   blog/models.py
        new file:   blog/tests.py
        new file:   blog/views.py
        modified:   config/settings.py

        NOTE: :)


#### 3. Create home page: View, Template and Urls

        new file:   blog/templates/blog/index.html
        new file:   blog/urls.py
        modified:   blog/views.py
        modified:   config/urls.py

        NOTE: :)


#### 4. Add template theme to home page

        modified:   README.md
        modified:   blog/templates/blog/index.html

        NOTE: :)


#### 5. Add and load static and media files

        modified:   README.md
        modified:   blog/templates/blog/index.html
        modified:   config/settings.py
        new file:   config/static/css/_button.css
        ...
        new file:   config/static/vendors/owl-carousel/owl.carousel.min.js
        modified:   config/urls.py

        NOTE: Slider loaded but does not sliding :)


#### 6. Base View - TemplateView: Rendering homepage using TemplateView

        modified:   README.md
        modified:   blog/urls.py
        modified:   blog/views.py

        NOTE: :)


#### 7. Create and extending base template

        modified:   README.md
        new file:   blog/templates/base.html
        modified:   blog/templates/blog/index.html       

        NOTE: :)


#### 8. Create include files for home page      

        modified:   README.md
        new file:   blog/templates/blog/inc/content_aside.html
        new file:   blog/templates/blog/inc/content_main.html
        new file:   blog/templates/blog/inc/slider.html
        modified:   blog/templates/blog/index.html
        
        NOTE: :)


#### 9. Create shared files for the base template

        modified:   README.md
        modified:   blog/templates/base.html
        new file:   blog/templates/shared/footer.html
        new file:   blog/templates/shared/head.html
        new file:   blog/templates/shared/header.html
        new file:   blog/templates/shared/scripts.html
        
        NOTE: :)


#### 10. Create page title using block tags

        modified:   README.md
        modified:   blog/templates/base.html
        modified:   blog/templates/shared/head.html
        
        NOTE: :)


#### 11. Create Post model and run migrations

        modified:   README.md
        new file:   blog/migrations/0001_initial.py
        modified:   blog/models.py
        
        NOTE: :)


#### 12. Defining how the Post model display in admin panel, and insert some posts

        modified:   README.md
        modified:   blog/admin.py
        new file:   media/uploads/posts/2022/01/27/m-blog-1.jpg
        new file:   media/uploads/posts/2022/01/27/m-blog-2.jpg
        new file:   media/uploads/posts/2022/01/27/m-blog-3.jpg
        
        NOTE: :)


#### 13. Generic display views - Load and fetch posts using ListView

        modified:   README.md
        modified:   blog/templates/blog/inc/content_main.html
        modified:   blog/templates/blog/index.html
        modified:   blog/urls.py
        modified:   blog/views.py
        new file:   media/uploads/posts/2022/01/27/blog-1.jpg
        new file:   media/uploads/posts/2022/01/27/blog-2.jpg
        new file:   media/uploads/posts/2022/01/27/blog-3.jpg
        
        NOTE: :)


#### 14. Generic display views - Filter posts by status published

        modified:   README.md
        modified:   blog/templates/blog/index.html
        modified:   blog/views.py
        new file:   media/uploads/posts/2022/01/27/blog-1_IuZm8eB.jpg
        new file:   media/uploads/posts/2022/01/27/blog-1_TIFIANn.jpg
        new file:   media/uploads/posts/2022/01/27/blog-2_6DLn1oe.jpg
        new file:   media/uploads/posts/2022/01/27/blog-3_V77GBfp.jpg
        new file:   media/uploads/posts/2022/01/27/blog-4.jpg
        new file:   media/uploads/posts/2022/01/27/blog-4_259KB2A.jpg
        
        NOTE: :)



### PAGINATION
--------------


#### 15. Pagination Part 1 - Make pagination as shared file to include in home page

        modified:   README.md
        modified:   blog/templates/blog/inc/content_main.html
        new file:   blog/templates/blog/shared/pagination.html      
        
        NOTE: :)


#### 16. Pagination Part 2 - Paginating the page

        modified:   README.md
        modified:   blog/templates/blog/shared/pagination.html
        modified:   blog/views.py
        
        NOTE: :)



### POST DETAIL
---------------


### 17. Post Detail Part 1: View, Template, Urls

        modified:   README.md
        modified:   blog/templates/blog/inc/content_main.html
        new file:   blog/templates/blog/post_detail.html
        modified:   blog/urls.py
        modified:   blog/views.py
        
        NOTE: :)