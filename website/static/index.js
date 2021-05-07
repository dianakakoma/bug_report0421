// report delete function that redirects to the homepage via a javascript request to the backend

function deleteReport(reportId){
    fetch('/delete-report', {
        method: 'POST',
        body: JSON.stringify({ reportId: reportId }),
    }).then((_res) => {window.location.href ='/';});
}