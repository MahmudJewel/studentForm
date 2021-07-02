from django.shortcuts import render, redirect
from second import models
from .models import stform

def htmlfile(request):
	#docid = int (request.GET.get('docid', 0))
	b=request.GET.get('docid',0)
	docid = int (b)
	print('value=',b,'type=', type(b))
	print('value=',docid,'type=', type(docid))
	documents = stform.objects.all()

###Start click and show data
	if docid>0:
		document=stform.objects.get(pk=docid)

	else:
		document=''

	print('document student form is ',document, docid)

	context={
		'docid' : docid,
		'documents' : documents,
		'document' : document
	}
### end click and show data.


### start edit and new save.
	if request.method=='POST':
		docid=int(request.POST.get('docid', 0))
		sid=request.POST.get('htmlId')
		name=request.POST.get('htmlName')
		DOB=request.POST.get('htmlDOB')
		gender=request.POST.get('htmlGender')
		address=request.POST.get('htmlAddress')
		zip=request.POST.get('htmlZip')

		if docid>0:
			document=stform.objects.get(pk=docid)
			document.sid=sid
			document.name=name
			document.DOB=DOB
			document.gender=gender
			document.addess=address
			document.zip_code=zip
			document.save()
			return redirect('/?docid=%i'%docid)

		else:
			document=stform.objects.create(sid=sid, name=name, DOB=DOB, gender=gender, addess=address, zip_code=zip)
			return redirect ('/?docid=%i' %document.id)

		#dt=models.stform(sid=sid, name=name, DOB=DOB, gender=gender, addess=address, zip_code=zip)
		#dt.save()
		
		print("Data saved in database")
### End edit and new save.

	return render(request,'index.html',context)

def delete_note(request, docid):
	print('Deleted docid', docid)
	document=stform.objects.get(pk=docid)
	document.delete()
	print('Deleted')
	return redirect('/?docid=0')

