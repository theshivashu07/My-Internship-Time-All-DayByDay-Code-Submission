from django.urls import path
from . import views

urlpatterns=[
		path('',views.index,name='index'),
		path('index/',views.index,name='index'),


		path('onlysum202105261/',views.onlysum202105261,name='onlysum202105261'),
		path('onlysum202105261/onlysum202105262',views.onlysum202105262,name='onlysum202105262'),

		path('checkprime202105261/',views.checkprime202105261,name='checkprime202105261'),
		path('checkprime202105261/checkprime202105262',views.checkprime202105262,name='checkprime202105262'),

		path('factorial202105261/',views.factorial202105261,name='factorial202105261'),
		path('factorial202105261/factorial202105262',views.factorial202105262,name='factorial202105262'),
	
		path('middleno202105261/',views.middleno202105261,name='middleno202105261'),
		path('middleno202105261/middleno202105262',views.middleno202105262,name='middleno202105262'),

		path('largestno202105261/',views.largestno202105261,name='largestno202105261'),
		path('largestno202105261/largestno202105262',views.largestno202105262,name='largestno202105262'),

		path('markseetstudent202105261/',views.markseetstudent202105261,name='markseetstudent202105261'),
		path('markseetstudent202105261/markseetstudent202105262',views.markseetstudent202105262,name='markseetstudent202105262'),


#--------------------------------------------------------------------------------------------------------------------------


		path('onlysum202105271/',views.onlysum202105271,name='onlysum202105271'),
		path('onlysum202105271/onlysum202105272',views.onlysum202105272,name='onlysum202105272'),

		path('checkprime202105271/',views.checkprime202105271,name='checkprime202105271'),
		path('checkprime202105271/checkprime202105272',views.checkprime202105272,name='checkprime202105272'),

		path('factorial202105271/',views.factorial202105271,name='factorial202105271'),
		path('factorial202105271/factorial202105272',views.factorial202105272,name='factorial202105272'),
	
		path('middleno202105271/',views.middleno202105271,name='middleno202105271'),
		path('middleno202105271/middleno202105272',views.middleno202105272,name='middleno202105272'),

		path('largestno202105271/',views.largestno202105271,name='largestno202105271'),
		path('largestno202105271/largestno202105272',views.largestno202105272,name='largestno202105272'),

		path('markseetstudent202105271/',views.markseetstudent202105271,name='markseetstudent202105271'),
		path('markseetstudent202105271/markseetstudent202105272',views.markseetstudent202105272,name='markseetstudent202105272'),



		#path('/',views.,name=''),
		#path('//',views.,name=''),

]

