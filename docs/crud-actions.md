# CRUD-Actions

CRUD is an acronym that stands for Create, Read, Update, and Delete. It refers to the four basic functions that are
essential in many database systems and applications for managing data. These operations are used to interact with the
data stored in a database or other data storage systems. Let's look at each operation:

- **Create (C):** This operation involves adding new data or records to the database. It allows you to insert new
  information into the system, creating a new entry.

- **Read (R):** This operation is used to retrieve or access data from the database. It allows you to view or fetch
  information from the existing records without altering or modifying them.

- **Update (U):** This operation allows you to modify or edit existing data in the database. You can change specific
  fields or properties of a record without creating a new one.

- **Delete (D):** This operation is used to remove data or records from the database. It allows you to permanently
  remove information that is no longer needed or relevant.

## Delete record

1. Add the url `path('delete_record/<int:pk>', views.delete_customer_record, name="delete_record")`
   to [urls.py](../dcrm/website/urls.py)
2. To delete the record add the delete_customer_record-view:

```python
def delete_customer_record(request, pk):
    if request.user.is_authenticated:
        Record.objects.get(id=pk).delete()
        messages.success(request, "Record deleted successfully")
        return redirect('home')
    else:
        messages.success(request, "Please log in!")
        return redirect('home')
```

3. Add the delete-button to the record-template:

```html

<div class="card-footer">
    <a class="btn btn-danger" href="{% url 'delete_record' record.id %}">Delete</a>
</div>
```

## Add record

1. Add url in [urls.py](../dcrm/website/urls.py)
2. Add view in [views.py](../dcrm/website/views.py)
3. Create template [add_record.html](../dcrm/website/templates/add_record.html)
4. Add "Create record"-button to home

## Update record

1. Add url in [urls.py](../dcrm/website/urls.py)
2. Add view in [views.py](../dcrm/website/views.py)
3. Create template [update_record.html](../dcrm/website/templates/update_record.html)
4. Add "Edit record"-button to record card

