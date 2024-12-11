document.addEventListener("DOMContentLoaded", function() {
    // Edit Comment
    const editBtns = document.querySelectorAll('.edit-btn');
    editBtns.forEach(button => {
        button.addEventListener('click', function() {
            const commentId = this.dataset.commentId;
            const commentBody = document.getElementById(`comment-body-${commentId}`).textContent;
            const commentImage = document.getElementById(`comment-image-${commentId}`);

            // Use SweetAlert2 to show a prompt with an input field
            Swal.fire({
                title: 'Edit your comment',
                input: 'textarea',  // Use textarea for multi-line input
                inputValue: commentBody,
                inputPlaceholder: 'Enter your comment...',
                showCancelButton: true,
                confirmButtonText: 'Save',
                cancelButtonText: 'Cancel',
                confirmButtonColor: '#FED154',
                customClass: 'swal-background',
                inputAttributes: {
                    'poppins': 'Type your comment here'
                },
                preConfirm: (newBody) => {
                    if (!newBody.trim()) {
                        Swal.showValidationMessage('Comment cannot be empty');
                    } else {
                        return newBody;  // return the new comment
                    }
                }
            }).then((result) => {
                if (result.isConfirmed) {
                    const newBody = result.value;
                    const formData = new FormData();
                    formData.append('comment_body', newBody);
                    if (commentImage) {
                        const newImage = commentImage.files ? commentImage.files[0] : null;
                        if (newImage) {
                            formData.append('comment_image', newImage);
                        }
                    }

                    fetch(`/homepage/edit-comment/${commentId}/`, {
                        method: 'POST',
                        headers: {
                            'X-CSRFToken': csrf_token
                        },
                        body: formData
                    }).then(response => response.json())
                    .then(data => {
                        if (data.status === 'success') {
                            document.getElementById(`comment-body-${commentId}`).textContent = data.comment_body;
                            if (data.comment_image_url) {
                                document.getElementById(`comment-image-${commentId}`).src = data.comment_image_url;
                            }
                            Swal.fire({
                                icon: 'success',
                                title: 'Comment updated successfully!',
                                showConfirmButton: false,
                                timer: 9000,
                                customClass: 'swal-background',
                            });
                            window.location.href = `/homepage/views/${artwork_pk}/`; // Redirect back to the view page
                        } else {
                            Swal.fire({
                                icon: 'error',
                                title: 'Error editing comment.',
                                text: data.message || 'Something went wrong.',
                                showConfirmButton: true,
                                confirmButtonColor: '#FED154',
                                customClass: 'swal-background',
                            });
                        }
                    });
                }
            });
        });
    });

    // Delete Comment
    const deleteBtns = document.querySelectorAll('.delete-btn');
    deleteBtns.forEach(button => {
        button.addEventListener('click', function() {
            const commentId = this.dataset.commentId;

            Swal.fire({
                title: 'Are you sure?',
                text: "You won't be able to revert this!",
                icon: 'warning',
                showCancelButton: true,
                confirmButtonText: 'Yes, delete it!',
                cancelButtonText: 'No, cancel!',
                customClass: 'swal-background',
                confirmButtonColor: '#FED154'
            }).then((result) => {
                if (result.isConfirmed) {
                    fetch(`/homepage/delete-comment/${commentId}/`, {
                        method: 'DELETE',
                        headers: {
                            'X-CSRFToken': csrf_token
                        }
                    }).then(response => response.json())
                    .then(data => {
                        if (data.status === 'success') {
                            document.getElementById(`comment-${commentId}`).remove();
                            Swal.fire({
                                icon: 'success',
                                title: 'Comment deleted successfully!',
                                showConfirmButton: false,
                                timer: 5000,
                                customClass: 'swal-background'
                            });
                            window.location.href = `/homepage/views/${artwork_pk}/`; // Redirect back to the view page
                        } else {
                            Swal.fire({
                                icon: 'error',
                                title: 'Error deleting comment.',
                                text: data.message || 'Something went wrong.',
                                showConfirmButton: true,
                                customClass: 'swal-background',
                                confirmButtonColor: '#FED154',
                            });
                        }
                    });
                }
            });
        });
    });
});
