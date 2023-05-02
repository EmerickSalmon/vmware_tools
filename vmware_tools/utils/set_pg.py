from pyVmomi import vim

def manage_vm_tags(content, vm, tag_name, add_tag=True):
    # Retrieve the "custom" tag category
    cat_manager = content.tagCategoryManager
    categories = cat_manager.categoryList
    custom_category = None

    for cat in categories:
        if cat.name == "custom":
            custom_category = cat
            break

    if not custom_category:
        # Create the "custom" tag category if it does not exist
        custom_category = cat_manager.CreateCategory("custom", "Custom tag category", "VirtualMachine")

    # Retrieve the list of tags for the "custom" category
    tag_manager = content.tagManager
    tags = tag_manager.tagList

    # Search for the specified tag in the list of tags
    tag_to_manage = None
    for tag in tags:
        if tag.name == tag_name and tag.categoryId == custom_category.key:
            tag_to_manage = tag
            break

    if not tag_to_manage:
        # Create the tag if it does not exist
        tag_to_manage = tag_manager.CreateTag(tag_name, custom_category.key)

    # Check if the tag is already associated with the VM
    associated_tags = tag_manager.ListAttachedTags(vm)

    if add_tag:
        if tag_to_manage.key not in associated_tags:
            # Add the tag to the VM if it is not already associated
            tag_manager.AttachTag(tag_to_manage.key, vm)
            print(f"The tag '{tag_name}' has been added to the VM '{vm.name}'.")
        else:
            print(f"The tag '{tag_name}' is already associated with the VM '{vm.name}'.")
    else:
        if tag_to_manage.key in associated_tags:
            # Remove the tag from the VM if it is associated
            tag_manager.DetachTag(tag_to_manage.key, vm)
            print(f"The tag '{tag_name}' has been removed from the VM '{vm.name}'.")
        else:
            print(f"The tag '{tag_name}' is not associated with the VM '{vm.name}'.")
