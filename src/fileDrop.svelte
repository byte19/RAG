<script>
  let filename = ''
  let arr = []
  let fileToUpload
  let isLoading = false;

  // Handle file input change
  function handleFileChange(event) {
    const file = event.target.files[0]
    if (file) {
      filename = file.name
      arr = [...arr, filename]
      fileToUpload = file
      console.log('Selected files:', arr)
    }
  }

  // Function to send file to backend
  async function uploadFile() {
    isLoading = true;
    if (!fileToUpload) {
      console.error('No file selected.')
      return
    }

    const formData = new FormData()
    formData.append('file', fileToUpload)

    try {
      const response = await fetch('http://127.0.0.1:5000/upload', {
        // updated endpoint
        method: 'POST',
        body: formData,
      })

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }

      const result = await response.json()
      console.log('File processed:', result)
      alert(`File uploaded: ${result.message}`)
    } catch (error) {
      console.error('Error uploading file:', error)
    } finally {
            isLoading = false;
    }

  }
</script>

<main>
  <form on:submit|preventDefault={uploadFile}>
    <label>
      <input name="file" type="file" on:change={handleFileChange} />
      {#if filename}
        {#each arr as file}
          <p>{file}</p>
        {/each}
      {/if}
    </label>
    {#if isLoading}
      <div class="loading-screen">
        <p>Loading, please wait...</p>
      </div>
    {/if}
    <button type="submit">Upload File</button>
  </form>
</main>
